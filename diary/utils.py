import jwt
from django.http import JsonResponse
from config.settings import SECRET_KEY
from user.models import User


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user_id = User.objects.get(id = payload['user_id'])
            request.user = user_id
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'Token Error'}, status=400)
        
        except:
            return JsonResponse({'message': 'Error'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper