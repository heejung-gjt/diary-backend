# Daily Photo Diary v2.0
![what](https://user-images.githubusercontent.com/64240637/139034410-0f598095-ec7c-429c-bbdb-7c033a71c79c.png)

#### ➡️ [Front-End Github Repository](https://github.com/heejung-gjt/diary-frontend)

<br>

## 📖 초반 개발 환경
### [초기에 진행했던 프로젝트 보러가기](https://github.com/heejung-gjt/Toy-Project)

- 동료와 바닐라 JavaScript를 이용한 Toy Project 진행     
- 백엔드와 프론트엔드가 분리되어 있지 않고 따로 DB를 두지않아 localStorage에 데이터를 저장    

## 🧑‍🤝‍🧑 목표
- 프론트와 백엔드를 분리하여 프로젝트를 진행하여 배포해보고 싶습니다.  
- OAuth social login JWT 기반 인증 방식으로 로그인을 구현하고 싶습니다.
- login_check라는 데코레이터를 만들어 유저를 인가하고 싶습니다.   
- 유저를 초대하여 함께 쓸 수 있는 diary공간을 개발하고 싶습니다.          

<br>

## 연동방식
![연동방식](https://user-images.githubusercontent.com/64240637/139037056-e753b6ab-68d7-4d94-b9a4-9e17758b22f8.png)

1. client server간 data연동은 json포맷으로 진행
2. data저장은 서버 측의 db(후에 mysql로 변경 예정)에 저장
3. ajax기능을 사용해 데이터 요청을 전송, 반환
4. JsonResponse를 사용해 데이터 응답

<br>

## History

[wiki](https://github.com/heejung-gjt/diary-backend/wiki)   