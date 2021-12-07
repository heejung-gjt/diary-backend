from django.urls import path
from .views import ArticleView, ArticleDetailView

urlpatterns = [
    path("", ArticleView.as_view()),
    path("/detail", ArticleDetailView.as_view(), name="detail"),
    path("/<id>", ArticleDetailView.as_view(), name="update"),
    path("/delete/<id>", ArticleDetailView.as_view(), name="delete"),
]

