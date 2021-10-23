from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.generic import View
from diary.models import Article
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME,AWS_S3_REGION_NAME, STATIC_URL
from boto3.session import Session
from datetime import datetime
import boto3
import time


class ArticleView(View):
    def get(self, request, **kwargs):
        articles = Article.objects.values('id', 'title', 'created_at', 'image')
       
        return JsonResponse({'articles':list(articles)}, safe=False)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        s3_url = "https://django-diary-bucket.s3.ap-northeast-2.amazonaws.com/"
        client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        bucket = AWS_STORAGE_BUCKET_NAME
        now = datetime.now().strftime('%Y%H%M%S')
        client.upload_fileobj(
            file,
            bucket,
            now+file.name,
            ExtraArgs={
                    "ContentType": file.content_type,
            }
        )
        Article.objects.create(
        title = title,
        content = content,
        image = s3_url+now+file.name,
        created_at = time.time()
        )  
        return JsonResponse({'message': 'success'}, status=200)


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        print('흐므므믐')
        id = request.GET.get('id')
        article = Article.objects.filter(id = id).values('id', 'title', 'content', 'image', 'created_at', 'updated_at')
        print(article)
        return JsonResponse({'article':list(article)}, status=200)


class ArticleUpdateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        Article.objects.filter(id = data['id']).update(
            title = data['title'],
            content = data['content'],
            updated_at = time.time()
        )
        article = Article.objects.filter(id = data['id']).values('id', 'title', 'content', 'created_at', 'image', 'updated_at')
        return JsonResponse({'article': list(article)}, status=200)


class ArticleDeleteView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        Article.objects.filter(id = data['id']).delete()
        articles = Article.objects.all().values('id', 'title', 'created_at', 'image', 'updated_at')
        print('aaaa',articles, len(articles))
        return JsonResponse({'articles': list(articles)}, status=200)

