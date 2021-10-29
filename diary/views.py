import json
from django.http import JsonResponse
from django.http.response import ResponseHeaders
from django.views.generic import View
from diary.models import Article
from diary.utils import login_check
from .services import ArticleService, UploadImageService
from .dto import ArticleCreateDto, ArticleIdDto, ArticleUpdateDto
from user.models import User

class ArticleView(View):

    @login_check
    def get(self, request, **kwargs):
        articles = ArticleService.articles(request.user.pk)
        user_infor = User.objects.filter(pk=request.user.pk).values('userid')
        return JsonResponse({'articles':list(articles), 'user':list(user_infor)}, safe=False)

class ArticleCreateView(View):
    
    @login_check
    def post(self, request, *args, **kwargs):
        print('헐..')
        data = self._build_article_infor(request)
        image_url = UploadImageService.upload(data)
        ArticleService.create(data, image_url)
        return JsonResponse({'message': 'success'}, status=200)

    def _build_article_infor(self, request):
        print(request.user.pk)
        return ArticleCreateDto(
            file = request.FILES.get('image'),
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            user_pk  = request.user.pk
        )


class ArticleDetailView(View):

    @login_check
    def get(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        article = ArticleService.filter_article(data)
        return JsonResponse({'article':list(article)}, status=200)
    
    def _build_article_id(self, request):
        return ArticleIdDto(
            id = request.GET.get('id'),
            user_pk = request.user.pk
        )


class ArticleUpdateView(View):

    def post(self, request, *args, **kwargs):
        data = self._build_article_infor(request)
        image_url = UploadImageService.upload(data)
        ArticleService.update(data, image_url)
        article = ArticleService.filter_article(data)
        return JsonResponse({'article':list(article)}, status=200)

    def _build_article_infor(self, request):
        return ArticleUpdateDto(
            id = request.POST.get('id'),
            file = request.FILES.get('image'),
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )


class ArticleDeleteView(View):

    @login_check
    def post(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        ArticleService.delete(data)
        articles = ArticleService.articles(data.user_pk)
        return JsonResponse({'articles': list(articles)}, status=200)

    def _build_article_id(self, request):
        data = json.loads(request.body)
        return ArticleIdDto(
            id = data['id'],
            user_pk = request.user.pk
        )