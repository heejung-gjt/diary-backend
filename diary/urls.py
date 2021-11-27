
from django.urls import path
from .views import ArticleView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path("", ArticleView.as_view()),
    path("/delete", ArticleDeleteView.as_view(), name="delete"),
    path("/detail", ArticleDetailView.as_view(), name="detail"),
    path("/update", ArticleUpdateView.as_view(), name="detail"),
]
