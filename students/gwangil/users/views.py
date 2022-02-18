import json
from sys          import exec_prefix
from django.http  import JsonResponse
from django.views import View
from .models      import User
from .validation  import email_validation, password_validation


# http://127.0.0.1:8000/users/
class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            first_name   = data["first_name"]
            last_name    = data["last_name"]
            email        = data["email"]
            password     = data["password"]
            phone_number = data["phone_number"]

            if email_validation == False:
                return JsonResponse( {"message" : "INVALID_EMAIL❌"}, status = 403)
                
            if password_validation == False:
                return JsonResponse( {"message" : "INVALID_PASSWORD❌"}, status = 403)

            if User.objects.filter(email = email).exists():
                return  JsonResponse( {"message" : "Email Already Exists❗️"}, status = 400)

            User.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )
                    
            return JsonResponse( {"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse( {"message" : "KeyError😿"}, status = 400)

    def get(self, request):
        users = User.objects.all()
        result = []
        for user in users:
            s = {
                "name"         : user.first_name + user.last_name,
                "email"        : user.email,
                "password"     : user.password,
                "phone_number" : user.phone_number
            }
            result.append(s)
        return JsonResponse( {"message" : result}, status = 200 )

