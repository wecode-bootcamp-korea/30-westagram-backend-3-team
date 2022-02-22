import json, bcrypt ,jwt

from django.http  import JsonResponse
from django.views import View

from .models      import User
from .vaildators  import vaildate_email, vaildate_password
from my_settings  import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email           = data['email']
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            if vaildate_email(email)==None:
                return JsonResponse({"message":"WRONG FORMAT: e-mail"}, status=400)
            if vaildate_password(data['password'])==None:
                return JsonResponse({"message":"WRONG FORMAT: password"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message":"this email already exists"},status=400)
            
            User.objects.create(
                last_name    = data['last_name'],
                first_name   = data['first_name'],
                email        = email,
                password     = hashed_password,
                phone_number = data.get('phone_number',''),
            )
            return JsonResponse({'messasge':'created'}, status=201)
        except KeyError:
            return JsonResponse({"message":"KEYERROR"}, status=400)
    
class SignInView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email           = data['email']
            password        = data['password']
            user            = User.objects.get(email-email)
            hashed_password = user.password
            access_token    = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM)
            
            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')): 
                return JsonResponse({"message":"INVALID_USER"}, status=401) 
                
            return JsonResponse({"message":"SUCCESS", "access_token":access_token}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEYERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)