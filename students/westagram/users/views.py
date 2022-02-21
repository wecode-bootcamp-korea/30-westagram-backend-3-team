import json
import bcrypt

from django.http  import JsonResponse
from django.views import View

from users.validation import validate_email, validate_password
from users.models     import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            username         = data.get('username')
            email            = data.get('email')
            password         = data.get('password')
            contact          = data.get('contact', "")
            decoded_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if validate_email(email) == False:
                return JsonResponse({'messasge':'INVALID EMAIL'}, status=400) 

            if validate_password(password) == False:
                return JsonResponse({'messasge':'INVALID PASSWORD'}, status=400) 

            if User.objects.filter(email = email).exists():
                return JsonResponse({'messasge':'EXISTING USER'}, status=400)
                
            User.objects.create(
                username = username,
                email    = email,
                password = decoded_password,
                contact  = contact,
            )
            
            return JsonResponse({'messasge':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400) 

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email = email, password = password).exists():
                return JsonResponse({'message' : 'INVALID_USER'},status=401) 
        
            return JsonResponse({'message' : 'SUCCESS'},status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400)