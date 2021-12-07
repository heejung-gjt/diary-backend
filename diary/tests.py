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

        Article.objects.create(
            id=1,
            writer_id=1,
            title="테스트타이틀",
            content="테스트컨텐츠",
            image="img.png",
            created_at = "1638018629.919184"
        )

    def tearDown(self):
        Article.objects.all().delete()
        User.objects.all().delete()

    def test_get_article_success(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        response = self.client.get("/article", **header, content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "articles": 
                [{
                    "created_at": "1638018629.919184",
                    "id": 1,
                    "image": "img.png",
                    "title": "테스트타이틀"
                }],
            "user": "test1"
            })  

    def test_post_article_success(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", "rb") as myfile1:
          response = self.client.post("/article", {"image": myfile1, "title": "첫번째 타이틀", "content": "내용입니다"}, **header)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})  

    def test_post_article_invalid_input(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", "rb") as myfile1:
          response = self.client.post("/article", {"image": myfile1, "titles": "첫번째 타이틀", "content": "내용입니다"}, **header)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "INVALID INPUT"})  


class ArticleDetailTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create(id=1, userid="test1", password=bcrypt.hashpw("test1".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))
        
        self.user1_token = jwt.encode({"user_id": self.user1.id}, SECRET_KEY, ALGORITHM)
        
        self.user2 = User.objects.create(id=2, userid="test2", password=bcrypt.hashpw("test2".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))
        
        self.user2_token = jwt.encode({"user_id": self.user2.id}, SECRET_KEY, ALGORITHM)

        Article.objects.create(
            id=1,
            writer_id=1,
            title="테스트타이틀",
            content="테스트컨텐츠",
            image="img.png",
            created_at = "1638018629.919184"
        )

    def tearDown(self):
        Article.objects.all().delete()
        User.objects.all().delete()

    def test_get_detail_article_success(self):
        header = {"HTTP_Authorization": self.user1_token}
        
        response = self.client.get("/article/detail?article_id=1", **header, content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "article": [{
                        "content": "테스트컨텐츠",
                        "created_at": "1638018629.919184",
                        "id": 1,
                        "image": "img.png",
                        "title": "테스트타이틀",
                        "updated_at": ""
                        }]
                    })

    def test_get_detail_article_no_permission(self):
        header = {"HTTP_Authorization": self.user2_token}
        
        response = self.client.get("/article/detail?article_id=1", **header, content_type="application/json")
        
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"message": "NO PERMISSION"})

    def test_put_article_success(self):
            header = {"HTTP_Authorization": self.user1_token}
            
            with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", "rb") as myfile1:
                data = {
                    "image": myfile1, 
                    "title": "수정한 첫번째 타이틀", 
                    "content": "수정한 내용입니다"
                    }

                response = self.client.post("/article/1", data, **header)
            
            self.assertEqual(response.status_code, 200)

    def test_put_article_no_permission(self):
        header = {"HTTP_Authorization": self.user2_token}
        
        with open("/home/heejung/Desktop/프로젝트 이미지들/오늘 머했지.png", "rb") as myfile1:
            data = {
                "image": myfile1, 
                "title": "수정한 타이틀", 
                "content": "수정한 내용입니다"
                }

            response = self.client.post("/article/1", data, **header)
        
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"message": "NO PERMISSION"})

    def test_delete_article_success(self):
            header = {"HTTP_Authorization": self.user1_token}

            response = self.client.delete("/article/delete/1", **header)
            
            self.assertEqual(response.status_code, 200)

    def test_delete_article_no_permission(self):
        header = {"HTTP_Authorization": self.user2_token}

        response = self.client.delete("/article/delete/1", **header)
        
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"message": "NO PERMISSION"})

    def test_delete_article_no_exist(self):
        header = {"HTTP_Authorization": self.user1_token}

        response = self.client.delete("/article/delete/2", **header)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "NO EXIST ARTICLE"})
