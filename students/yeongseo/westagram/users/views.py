import json, bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View

from users.models        import User
from users.validation    import email_validate, password_validate
from my_settings        import SECRET_KEY as SECRET, algorithm
# Create your views here.

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email           = data['email']
            password        = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if email_validate(email) == False:
                return JsonResponse({'message': "invalid email"}, status=400)

            if password_validate(password) == False:
                return JsonResponse({'message':'invalid password'}, status=400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message':'Duplicated email'}, status=400)

            User.objects.create(
                username       = data['username'],
                phone_number   = data.get("phone_number", ''),
                email          =  email,
                password       = hashed_password
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
  
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LogInView(View):
    def post(self, request):
        data      = json.loads(request.body)

        try:
            email       = data['email']
            password    = data['password']

            hashed_password = User.objects.get(email=email).password

            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode()): 
                return JsonResponse({"message":"INVALID_USER"}, status=401) 
            
            access_token = jwt.encode({'id': User.objects.get(email = email).id}, SECRET, algorithm=algorithm)

            return JsonResponse({'message':'SUCCESS', 'access_token': access_token}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)
