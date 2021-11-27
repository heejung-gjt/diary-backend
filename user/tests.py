import jwt
import json 
import bcrypt

from django.test import TestCase, Client

from user.models import User
from config.settings  import SECRET_KEY, ALGORITHM


class SignUpTest(TestCase):
    def setUp(self):
        self.client = Client()

        User.objects.create(userid="test2", password="qwerty2@")

    def tearDown(self):
        User.objects.all().delete()

    def test_post_signup_success(self):
        signup_data = {"username": "test1", "password": "qwerty1!"}
        response = self.client.post('/user/signup', json.dumps(signup_data), content_type='application/json')

        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})  

    def test_post_signup_already_exist_id(self):
        signup_data = {"username": "test2", "password": "qwerty1!"}

        response=self.client.post("/user/signup",json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "아이디가 존재합니다"})        

    def test_post_signup_invalid_id_type(self):
        signup_data = {"username": "tes", "password": "qwerty1!"}
        response=self.client.post("/user/signup",json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "아이디 형식이 틀립니다"})        

    def test_post_signup_invalid_password(self):
        signup_data = {"username": "test1", "password": "qwer"}
        response=self.client.post("/user/signup",json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "비밀번호 형식이 틀립니다"})   

    def test_post_signup_key_error(self):
        signup_data = {"usernames": "test1", "password": "qwerty1@"}
        response=self.client.post("/user/signin",json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "KEY ERROR"})  


class SignInTest(TestCase):
    def setUp(self):
        self.client = Client()

        user1 = User.objects.create(userid="test1", password=bcrypt.hashpw("qwerty1!".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))

        self.access_token1 = jwt.encode({"user_id": user1.id}, SECRET_KEY, ALGORITHM).decode("utf-8")

    def tearDown(self):
        User.objects.all().delete()

    def test_post_signin_success(self):
        signin_data = {"username": "test1", "password": "qwerty1!"}
        response = self.client.post("/user/signin", json.dumps(signin_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS", "token": self.access_token1})  

    def test_post_signin_invalid_id(self):
        signup_data = {"username": "test2", "password": "qwerty1!"}
        response=self.client.post("/user/signin", json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)

        self.assertEqual(response.json(), {"error" : "아이디 또는 비밀번호를 다시 입력해주세요"})  

    def test_post_signin_invalid_pwd(self):
        signup_data = {"username": "test1", "password": "qwerty@@"}
        response=self.client.post("/user/signin", json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "아이디 또는 비밀번호를 다시 입력해주세요"}) 

    def test_post_signin_key_error(self):
        signup_data = {"usernames": "test1", "password": "qwerty@@"}
        response=self.client.post("/user/signin", json.dumps(signup_data), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "KEY ERROR"})         
