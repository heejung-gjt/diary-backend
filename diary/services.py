from os import stat
import boto3
import time
from datetime import datetime
from diary.dto import ArticleIdDto, ArticleUpdateDto
from diary.models import Article
from .dto import ArticleCreateDto
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME,AWS_S3_REGION_NAME, STATIC_URL
from boto3.session import Session


class ArticleService():

    @staticmethod
    def articles():
        return Article.objects.values('id', 'title', 'created_at', 'image')

    @staticmethod
    def detail_article(id):
        return Article.objects.filter(id = id).values('id', 'title', 'content', 'created_at', 'image', 'updated_at')

    @staticmethod
    def filter_article(dto:ArticleIdDto):
        return Article.objects.filter(id = dto.id).values('id', 'title', 'content', 'image', 'created_at', 'updated_at')

    @staticmethod
    def create(dto:ArticleCreateDto, url):
        Article.objects.create(
        title = dto.title,
        content = dto.content,
        image = url,
        created_at = time.time()
        )  

    @staticmethod
    def delete(dto:ArticleIdDto):
        client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        bucket = AWS_STORAGE_BUCKET_NAME
        client.delete_object(
            Bucket= bucket,
            Key = Article.objects.get(id=dto.id).image.split('/')[-1]
        )
        Article.objects.filter(id = dto.id).delete()

    def update(dto:ArticleIdDto, file):
        if file:
            Article.objects.filter(id = dto.id).update(
            title = dto.title,
            content = dto.content,
            updated_at = time.time(),
            image =  file
            )
        else:
            Article.objects.filter(id = dto.id).update(
            title = dto.title,
            content = dto.content,
            updated_at = time.time(),
            )      


class UploadImageService():
    # s3에서 image 삭제후 업로드
    def upload(dto:ArticleUpdateDto):
        if not dto.__dict__['file'] == None:
            s3_url = "https://django-diary-bucket.s3.ap-northeast-2.amazonaws.com/"
            client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )
            bucket = AWS_STORAGE_BUCKET_NAME
            if 'id' in dto.__dict__:
                client.delete_object(
                    Bucket= bucket,
                    Key = Article.objects.get(id=dto.id).image.split('/')[-1]
                )
            now = datetime.now().strftime('%Y%H%M%S')
            client.upload_fileobj(
                dto.file,
                bucket,
                now+dto.file.name,
                ExtraArgs={
                        "ContentType": dto.file.content_type,
                })
            return s3_url+now+dto.file.name
        else:
            return False

