import json
from os import stat_result

from django.http import JsonResponse
from django.views.generic import View

from diary.dto import ArticleCreateDto, ArticleIdDto, ArticleUpdateDto
from core.utils import login_check
from diary.services import ArticleService, UploadImageService
from user.services import UserService


class ArticleView(View):
    @login_check
    def get(self, request):
        article_list = ArticleService.get_articles(request.user.pk)
        userid = UserService.get_userid(request.user.pk)

        context = {"articles": list(article_list), "user": userid}

        return JsonResponse(context, status=200)

    @login_check
    def post(self, request):
        data = self._build_article_info(request)
        
        if not (data.file and data.title and data.content):
            return JsonResponse({"error": "INVALID INPUT"}, status=400)
        
        image_url = UploadImageService.upload(data)

        ArticleService.create(data, image_url)
        
        return JsonResponse({"message": "SUCCESS"}, status=200)

    def _build_article_info(self, request):
            return ArticleCreateDto(
                file=request.FILES.get("image"),
                title=request.POST.get("title"),
                content=request.POST.get("content"),
                user_pk=request.user.pk
            )


class ArticleDetailView(View):

    @login_check
    def get(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        article = ArticleService.filter_article(data)
        return JsonResponse({"article":list(article)}, status=200)
    
    def _build_article_id(self, request):
        return ArticleIdDto(
            id = request.GET.get("id"),
            user_pk = request.user.pk
        )


class ArticleUpdateView(View):

    def post(self, request, *args, **kwargs):
        data = self._build_article_infor(request)
        image_url = UploadImageService.upload(data)
        ArticleService.update(data, image_url)
        article = ArticleService.filter_article(data)
        return JsonResponse({"article":list(article)}, status=200)

    def _build_article_infor(self, request):
        return ArticleUpdateDto(
            id = request.POST.get("id"),
            file = request.FILES.get("image"),
            title = request.POST.get("title"),
            content = request.POST.get("content")
        )


class ArticleDeleteView(View):

    @login_check
    def post(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        ArticleService.delete(data)
        articles = ArticleService.articles(data.user_pk)
        return JsonResponse({"articles": list(articles)}, status=200)

    def _build_article_id(self, request):
        data = json.loads(request.body)
        return ArticleIdDto(
            id = data["id"],
            user_pk = request.user.pk
        )
