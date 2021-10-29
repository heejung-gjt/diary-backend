from django.core.exceptions import ValidationError
from .models import User

def validate_id(id):
    if User.objects.filter(userid = id).exists():
        raise ValidationError(('아이디 존재'), code = 'invalid')
    if len(id) < 4:
        raise ValidationError(('아이디 형식 에러'), code = 'invalid')
    return id


def validate_pwd(pwd):
    if len(pwd) < 5:
        raise ValidationError(('비밀번호 형식 에러'), code = 'invalid')

    return pwd
