import json

from django.http  import JsonResponse
from django.views import View

from .models      import User
from .validation  import email_validation, password_validation



class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            first_name   = data["first_name"]
            last_name    = data["last_name"]
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]

            if not email_validation(email):
                if not password_validation(password):
                    return JsonResponse( {"message" : "INVALID_EMAIL & PASSWORD"}, status = 403)
                else:
                    return JsonResponse( {"message" : "INVALID_EMAIL"}, status = 403)
                
            if not password_validation(password):
                return JsonResponse( {"message" : "INVALID_PASSWORD"}, status = 403)

            if User.objects.filter(email = email).exists():
                return  JsonResponse( {"message" : "Email Already Exists"}, status = 400)

            User.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )
                    
            return JsonResponse( {"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse( {"message" : "KEYERROR"}, status = 400)


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email     = data["email"]
            password  = data["password"]
            
            if not User.objects.filter(password = password, email = email).exists():
                return JsonResponse( {"message" : "INVALID_USER"}, status = 401)

            return JsonResponse( {"massege" : "SUCCESS"}, status = 200)
        except KeyError:
            return JsonResponse( {"message" : "KEY_ERROR"}, status = 400)
