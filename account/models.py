from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'


class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        db_table = 'follow'