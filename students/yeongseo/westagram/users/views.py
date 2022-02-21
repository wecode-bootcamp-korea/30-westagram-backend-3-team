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

            if User.objects.get(email = email).exists():
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