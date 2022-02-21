import json

from django.http  import JsonResponse
from django.views import View

from users.validation import validate_email, validate_password
from users.models     import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            username = data['username']
            email    = data['email']
            password = data['password']
            contact  = data['contact']

            if validate_email(email) == False:
                return JsonResponse({'messasge':'INVALID EMAIL'}, status=400) 

            if validate_password(password) == False:
                return JsonResponse({'messasge':'INVALID PASSWORD'}, status=400) 

            if User.objects.filter(email = email).exists():
                return JsonResponse({'messasge':'EXISTING USER'}, status=400)
                
            User.objects.create(
                username = username,
                email    = email,
                password = password,
                contact  = contact,
            )
            
            return JsonResponse({'messasge':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400) 
