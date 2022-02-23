import json
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from users.validation import validate_email, validate_password
from users.models     import User, Follow
from my_settings      import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            username         = data.get('username')
            email            = data.get('email')
            password         = data.get('password')
            contact          = data.get('contact', "")
            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if validate_email(email) == False:
                return JsonResponse({'messasge':'INVALID EMAIL'}, status=400) 

            if validate_password(password) == False:
                return JsonResponse({'messasge':'INVALID PASSWORD'}, status=400) 

            if User.objects.filter(email = email).exists():
                return JsonResponse({'messasge':'EXISTING USER'}, status=400)
                
            User.objects.create(
                username = username,
                email    = email,
                password = hashed_password,
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

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'INVALID_USER'},status=401) 
        
            user            = User.objects.get(email = email)
            hashed_password = user.password.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                access_token = jwt.encode({'id':user.id}, SECRET_KEY, ALGORITHM)
                return JsonResponse({'message':'SUCCESS', 'access_token':access_token}, status=200)

            return JsonResponse({'message' : 'INCORRECT_PASSWORD'},status=401)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400)

class FollowView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            followuser_id   = data['followuser_id']
            followeduser_id = data['followeduser_id']

            if not User.objects.filter(id = followuser_id and followeduser_id).exists():
                return JsonResponse({'message' : 'INVALID_USER'},status=401) 

            if Follow.objects.filter(followeduser_id = followeduser_id).exists():
                return JsonResponse({'message' : 'You have already followed'},status=401) 

            if Follow.objects.filter(followuser_id = followeduser_id).exists():
                return JsonResponse({'message' : 'It is the same user'},status=401)

            Follow.objects.create(
                followuser_id   = followuser_id,
                followeduser_id = followeduser_id
            )
            
            return JsonResponse({'messasge':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400)