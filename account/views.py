import json
from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import User


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            name=data['name'],
            email=data['email'],
            password=data['password'],
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
                if user.password == data['password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'users':'invalid'}, status=401)