import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from .models      import User
from .validation  import email_validation, password_validation
from my_settings  import SECRET_KEY, ALGORITHM


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            first_name      = data["first_name"]
            last_name       = data["last_name"]
            email           = data["email"]
            password        = data["password"]
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            phone_number    = data.get("phone_number", "")

            if not email_validation(email) and not password_validation(password):
                    return JsonResponse( {"message" : "INVALID_EMAIL & PASSWORD"}, status = 403)
            elif not email_validation(email) :
                    return JsonResponse( {"message" : "INVALID_EMAIL"}, status = 403)
            elif not password_validation(password):
                return JsonResponse( {"message" : "INVALID_PASSWORD"}, status = 403)

            if User.objects.filter(email = email).exists():
                return  JsonResponse( {"message" : "Email Already Exists"}, status = 400)

            User.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = hashed_password,
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
        
            if not User.objects.filter(email = email).exists():
                return JsonResponse( {"message" : "INVALID_USER"}, status = 401)

            user = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse( {"message" : "INVALID_USER"}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
            
            return JsonResponse( {"massege" : "SUCCESS", "access_token" : access_token}, status = 200)
        except KeyError:
            return JsonResponse( {"message" : "KEY_ERROR"}, status = 400)
