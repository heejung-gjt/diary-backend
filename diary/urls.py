
from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('delete/', ArticleDeleteView.as_view(), name='delete'),
    path('detail/', ArticleDetailView.as_view(), name='detail'),
    path('update/', ArticleUpdateView.as_view(), name='detail'),
]
