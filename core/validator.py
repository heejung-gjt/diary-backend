from django.core.exceptions import ValidationError

from user.models import User

def validate_id(id):
    if User.objects.filter(userid = id).exists():
        raise ValidationError(('아이디가 존재합니다 !'), code = 'invalid')
    if len(id) < 4:
        raise ValidationError(('아이디 확인해주세요 !'), code = 'invalid')
    return id


def validate_pwd(pwd):
    if len(pwd) < 5:
        raise ValidationError(('비밀번호 확인해주세요 !'), code = 'invalid')
    return pwd
