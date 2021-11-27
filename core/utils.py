import jwt

from django.http import JsonResponse

from user.models import User
from config.settings import SECRET_KEY, ALGORITHM


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user_id = User.objects.get(id = payload["user_id"])
            request.user = user_id

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID TOKEN"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID USER"}, status=404)

        return func(self, request, *args, **kwargs)

    return wrapper
