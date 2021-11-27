import jwt
import bcrypt

from django.test import TestCase, Client
from diary.models import Article

from user.models import User
from config.settings  import SECRET_KEY, ALGORITHM


class ArticleTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create(id=1, userid="test1", password=bcrypt.hashpw("test1".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))
        
        self.user1_token = jwt.encode({"user_id": self.user1.id}, SECRET_KEY, ALGORITHM)

    def tearDown(self):
        Article.objects.all().delete()
        User.objects.all().delete()

    def test_post_article_success(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", 'rb') as myfile1:
          response = self.client.post('/article', {"image": myfile1, "title": "첫번째 타이틀", "content": "내용입니다"}, **header)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})  

    def test_post_article_invalid_input(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", 'rb') as myfile1:
          response = self.client.post('/article', {"image": myfile1, "titles": "첫번째 타이틀", "content": "내용입니다"}, **header)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "INVALID INPUT"})  
