import json
from django.http import JsonResponse
from django.views.generic import View
from diary.models import Article
from .services import ArticleService, UploadImageService
from .dto import ArticleCreateDto, ArticleIdDto, ArticleUpdateDto


class ArticleView(View):
    def get(self, request, **kwargs):
        articles = ArticleService.articles()
        return JsonResponse({'articles':list(articles)}, safe=False)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = self._build_article_infor(request)
        image_url = UploadImageService.upload(data)
        ArticleService.create(data, image_url)
        return JsonResponse({'message': 'success'}, status=200)

    def _build_article_infor(self, request):
        return ArticleCreateDto(
            file = request.FILES.get('image'),
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        article = ArticleService.filter_article(data)
        return JsonResponse({'article':list(article)}, status=200)
    
    def _build_article_id(self, request):
        return ArticleIdDto(
            id = request.GET.get('id')
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
    def post(self, request, *args, **kwargs):
        data = self._build_article_id(request)
        ArticleService.delete(data)
        articles = ArticleService.articles()
        return JsonResponse({'articles': list(articles)}, status=200)

    def _build_article_id(self, request):
        data = json.loads(request.body)
        return ArticleIdDto(
            id = data['id']
        )