from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView


class DiaryView(ListView):
    def get(self, request, **kwargs):
        print('왔ㅇ엉..')
        tmpList = [
       {'id': 4, 'title': "머리가 아푸다 흑흑", 'content': "내용4", 'date': "2021-04-06", 'edited':''},
       {'id': 3, 'title': "study.. 머리가 아푸다 흑흑", 'content': "내용2", 'date': "2021-04-05", 'edited':''},
       {'id': 2, 'title': "hard.. 머리가 아푸다 흑흑", 'content': "내용3", 'date': "2021-04-04", 'edited':''},
       {'id': 1, 'title': "okok 오예오예 어차차 머리가 아푸다 흑흑", 'content': "내용", 'date': "2021-04-03", 'edited':''},
   ]
        return JsonResponse(data=tmpList, safe=False)