from django.db import models


class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=512)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    lastmodified_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=512)

    class Meta:
        db_table = "blogs"
