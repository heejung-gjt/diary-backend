from user.models import User


class UserService():
    @staticmethod
    def get_userid(pk):
        return User.objects.get(pk=pk).userid
