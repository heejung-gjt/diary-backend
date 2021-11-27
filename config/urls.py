from django.urls import path, include
from diary.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='article'),
    path('article', include('diary.urls')),
    path('user', include('user.urls')),
]
