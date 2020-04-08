import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import User


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            user=User.objects.get(name=data['name']),
            comment=data['comment'],
        ).save()
        return HttpResponse(status=200)

    def get(self, request):
        comment = Comment.objects.values()
        return JsonResponse({'comments':list(comment)}, status=200)


class MyCommentView(View):
    def get(self, request, user_id):
        my_comment = []
        comments = Comment.objects.filter(user_id=user_id).values()
        for comment in comments:
            if comment['user_id'] == user_id:
                my_comment.append(comment['comment'])
        return JsonResponse({'comments': my_comment}, status=200)