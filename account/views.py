import json
import bcrypt
import jwt

from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import User
from wetargram.settings import SECRET_KEY



class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            name=data['name'],
            email=data['email'],
            password=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
        ).save()
        return HttpResponse(status=200)

    def get(self, request):
        user_data = User.objects.values()
        return JsonResponse({'users': list(user_data)}, status=200)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
                    return JsonResponse({'access_token': token.decode('utf-8')}, status=200)
                return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'users':'invalid'}, status=401)