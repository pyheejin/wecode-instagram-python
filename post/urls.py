from django.urls import path

from .views import CommentView, MyCommentView

app_name = 'post'

urlpatterns = [
    path('comments', CommentView.as_view()),
    path('comment/<int:user_id>', MyCommentView.as_view()),
]