
from django.urls import path
from .views import ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/', ArticleDetailView.as_view(), name='detail'),
]
