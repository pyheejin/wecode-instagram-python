import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import User
from .utils import login_decorator


class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        Comment(
            user = request.user,
            comment=data['comment'],
        ).save()
        print("request.user=", end=""), print(request.user)
        return HttpResponse(status=200)

    def get(self, request):
        comment = Comment.objects.values()
        return JsonResponse({'comments':list(comment)}, status=200)


class MyCommentView(View):
    def get(self, request, user_id):
        comments = Comment.objects.filter(user_id=user_id).values()
        return JsonResponse({'comments': list(comments)}, status=200)