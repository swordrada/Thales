from django.db import models


class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=512)
    content = models.TextField()
    user_id = models.IntegerField()
    click_time = models.BigIntegerField()
    image = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    lastmodified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blogs"


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=512)
    username = models.CharField(max_length=512)

    class Meta:
        db_table = "users"


class BlogComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.IntegerField()
    content = models.TextField()
    comment_username = models.CharField(max_length=512)
    create_time = models.DateTimeField(auto_now=True)
    lastmodified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog_comments"


class MessageBoard(models.Model):
    id = models.BigAutoField(primary_key=True)
    random_user = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    content = models.TextField()
    reply = models.TextField()
    reply_user_id = models.IntegerField()
    create_time = models.DateTimeField(auto_now=True)
    lastmodified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message_board"
