import json
import jwt
import bcrypt

from django.views.generic import View
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError

from user.models import User
from core.validator import validate_id, validate_pwd, validate_user_id, validate_user_pwd
from config.settings import ALGORITHM, SECRET_KEY


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            userid = validate_id(data["username"])
            password = validate_pwd(data["password"])

            hashed_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            
            User.objects.create(userid=userid, password=hashed_pwd)

            return JsonResponse({"message":"SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"error": "KEY ERROR"}, status=400)


        except ValidationError as e:
            return JsonResponse({"error": e.message}, status=400)


class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            userid  = validate_user_id(data["username"])
            password = validate_user_pwd(userid, data["password"])

            if password:
                token = jwt.encode({"user_id":userid.id}, SECRET_KEY, ALGORITHM).decode("utf-8")
            
            return JsonResponse({"message" : "SUCCESS", "token":token}, status=200)
                    
        except KeyError:
            return JsonResponse({"error": "KEY ERROR"}, status=400)


        except ValidationError as e:
            return JsonResponse({"error": e.message}, status=400)


