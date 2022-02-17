import json
import re #정규표현식

from django.shortcuts import render
from django.http       import JsonResponse
from django.views import View

from users.models import Users
# Create your views here.

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Users.objects.create(
            username = data['username']
            phone_number = data['phone_number']
        )
        if re.match("@", data['email']) and re.match(".",data["email"]):
            Users.objects.create(email=data['email'])
        else:
            return JsonResponse({'message': 'please include "@" and "." in your email'})
        #문자 , 숫자 , 특수문자 의 복합이도록 정규표현식 작성
        #입력받는 길이 # 영대소문자,숫자 가 있고, 영대소문자숫자 제외한것(특수문자) 가 있으면 
        if re.match('[a-zA-Z0-9]+', data['password']) and re.match('[^\sa-zA-Z0-9]+',data['password']):
            Users.objects.create(password=data['password'])
            



        return JsonResponse({'message':'SUCCESS'}, status=201)