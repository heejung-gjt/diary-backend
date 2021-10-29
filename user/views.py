import json
import jwt
import bcrypt
from django.core.exceptions import ValidationError
from django.http.response import JsonResponse
from django.views.generic import View
from config.settings import SECRET_KEY
from .validator import validate_id, validate_pwd

from .models import User


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        try:
            if User.objects.filter(userid=data['username']).exists():
                user = User.objects.get(userid=data['username'])

            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'user_id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                return JsonResponse({'token':token}, status=200)
            return JsonResponse({'message':'error'}, status=401)
        
        except KeyError:
            return JsonResponse({'message': 'Invalid Keys'}, status=400)


class SignUpView(View):


    def post(self, request):
        data = json.loads(request.body)
        try:
            userid = validate_id(data['username'])
            password = validate_pwd(data['password'])
            hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                userid = userid,
                password = hashed_pwd
            )
            return JsonResponse({'message':'Success'}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'Invalid Keys'}, status=400)

        except ValidationError as e:
            return JsonResponse({'message': e.message}, status=400)
