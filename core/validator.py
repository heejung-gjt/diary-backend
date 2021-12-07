import bcrypt

from django.core.exceptions import ValidationError

from user.models import User
from diary.models import Article

def validate_id(id):
    if User.objects.filter(userid = id).exists():
        raise ValidationError(('아이디가 존재합니다'), code='invalid')

    if len(id) < 4:
        raise ValidationError(('아이디 형식이 틀립니다'), code='invalid')

    return id


def validate_pwd(pwd):
    if len(pwd) < 5:
        raise ValidationError(('비밀번호 형식이 틀립니다'), code='invalid')

    return pwd


def validate_user_id(id):
    if not User.objects.filter(userid=id).exists():
        raise ValidationError(("아이디 또는 비밀번호를 다시 입력해주세요"), code="invalid")
    
    return User.objects.get(userid=id)


def validate_user_pwd(user, pwd):
    if not bcrypt.checkpw(pwd.encode('utf-8'), user.password.encode('utf-8')):

        raise ValidationError(("아이디 또는 비밀번호를 다시 입력해주세요"), code="invalid")
    
    return True


def validate_user_permission(id, user_id):
    if Article.objects.get(id=id).writer.id != user_id:
        
        return {"error": True}
    
    return {"error": False}