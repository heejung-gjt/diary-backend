import json

from django.http import JsonResponse
from django.views.generic import View

from diary.dto import ArticleCreateDto, ArticleIdDto, ArticleUpdateDto
from core.utils import login_check
from core.validator import validate_user_permission
from diary.models import Article
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
    def get(self, request):

        data = self._build_article_detail_id(request)
        
        user_permission = validate_user_permission(data.id, request.user.pk)
        
        if user_permission["error"]:
             return JsonResponse({"message": "NO PERMISSION"}, status=405)
        
        article = ArticleService.filter_article(data)

        return JsonResponse({"article":list(article)}, status=200)
    
    def _build_article_detail_id(self, request):
        return ArticleIdDto(
            id=request.GET.get("article_id"),
            user_pk=request.user.pk
        )

    @login_check
    def post(self, request, id):
        data = self._build_article_info(request, id)

        user_permission = validate_user_permission(data.id, request.user.pk)
        
        if user_permission["error"]:
             return JsonResponse({"message": "NO PERMISSION"}, status=405)

        image_url = UploadImageService.upload(data)
        
        is_updated = ArticleService.update(data, image_url)

        if is_updated["error"]:
            return JsonResponse({"message": "INVALID INPUT"}, status=404)

        article = ArticleService.filter_article(data)
        
        return JsonResponse({"article":list(article)}, status=200)

    def _build_article_info(self, request, id):
        return ArticleUpdateDto(
            id=id,
            file=request.FILES.get("image"),
            title=request.POST.get("title"),
            content=request.POST.get("content")
        )

