import json

from django.http     import JsonResponse
from django.views    import View

from users.models        import User
from users.validation    import email_validate, password_validate
# Create your views here.

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            if email_validate(email) == False:
                return JsonResponse({'message': "invalid email"}, status=400)

            if password_validate(password) == False:
                return JsonResponse({'message':'invalid password'}, status=400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message':'Duplicated email'}, status=400)

            User.objects.create(
                username       = data['username'],
                phone_number   = data['phone_number'],
                email          =  email,
                password       = password
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
  
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            login_email = data['email']
            password    = data['password']

            if not User.objects.filter(email=login_email).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)

            if password != User.objects.get(email=login_email).password:
                return JsonResponse({"message":"INVALID_USER"}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
