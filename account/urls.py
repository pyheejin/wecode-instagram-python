from django.urls import path

from .views import SignUpView, LoginView

app_name = 'account'

urlpatterns = [
    path('/login', LoginView.as_view()),
    path('/sign-up', SignUpView.as_view()),
]