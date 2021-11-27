import boto3
import time
from datetime import datetime

from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

from diary.dto    import ArticleCreateDto, ArticleIdDto, ArticleUpdateDto
from diary.models import Article


class ArticleService():
    @staticmethod
    def get_articles(pk):
        return Article.objects.filter(writer__pk=pk).values("id", "title", "created_at", "image")

    @staticmethod
    def detail_article(id):
        return Article.objects.filter(id = id).values("id", "title", "content", "created_at", "image", "updated_at")

    @staticmethod
    def filter_article(dto:ArticleIdDto):
        return Article.objects.filter(id = dto.id).values("id", "title", "content", "image", "created_at", "updated_at")

    @staticmethod
    def create(dto:ArticleCreateDto, url):
        Article.objects.create(
        writer_id=dto.user_pk,
        title=dto.title,
        content=dto.content,
        image=url,
        created_at=time.time()
        )

    @staticmethod
    def delete(dto:ArticleIdDto):
        client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        bucket = AWS_STORAGE_BUCKET_NAME
        client.delete_object(
            Bucket= bucket,
            Key = Article.objects.get(id=dto.id).image.split("/")[-1]
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
    def upload(dto:ArticleUpdateDto):
        s3_url = "https://django-diary-bucket.s3.ap-northeast-2.amazonaws.com/"
        
        client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        
        bucket = AWS_STORAGE_BUCKET_NAME
        
        if "id" in dto.__dict__: # 이미지 업데이트 경우
            client.delete_object(
                Bucket=bucket,
                Key=Article.objects.get(id=dto.id).image.split("/")[-1]
            )

        now = datetime.now().strftime("%Y%H%M%S")
        
        client.upload_fileobj(
            dto.file,
            bucket,
            now+dto.file.name,
            ExtraArgs={"ContentType": dto.file.content_type,}
            )
        
        return s3_url+now+dto.file.name


