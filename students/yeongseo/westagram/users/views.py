import json
import re

#from django.shortcuts import render
from django.http       import JsonResponse
from django.views import View
from django.db import IntegrityError

from users.models import Users
from users.validation import email_validate, password_validate
# Create your views here.



class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if email_validate(data['email']) == False:
                return JsonResponse({'message': "invalid email"}, status=400)

            if password_validate(data['password']) == False:
                return JsonResponse({'message':'invalid password'})

            Users.objects.create(
                username        = data['username'],
                phone_number = data['phone_number'],
                email             =  data['email'],
                password        = data['password']
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
  

        except IntegrityError: 
            return JsonResponse({'message':"Your email overlaps with other user's email"}, status=400)      
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)