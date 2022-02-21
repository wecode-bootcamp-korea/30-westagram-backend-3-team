import json, re

from django.http  import JsonResponse
from django.views import View

from .models import User
from .vaildators import vaildate_email, vaildate_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            
            if vaildate_email(email)==None:
                return JsonResponse({"message":"WRONG FORMAT: e-mail"}, status=400)
            if vaildate_password(password)==None:
                return JsonResponse({"message":"WRONG FORMAT: password"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"this email already exists"},status=400)
            
            User.objects.create(
                last_name    = data['last_name'],
                first_name   = data['first_name'],
                email        = email,
                password     = password,
                phone_number = data['phone_number'],
            )
        except KeyError:
            return JsonResponse({"message":"KEYERROR"}, status=400)
        return JsonResponse({'messasge':'created'}, status=201)
    
class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
                
        except KeyError:
            return JsonResponse({"message":"KEYERROR"}, status=400)
        return JsonResponse({"messasge":"SUCCESS"}, status=200)