from django.urls import path
from user.views import SigninView, SignUpView

urlpatterns = [
    path('/signin', SigninView.as_view()),
    path('/signup', SignUpView.as_view()),
]
