from inspiration.models import *


def create(req):
    Blogs.objects.create(title=req["title"], content=req["content"], author=req["author"])


def update(req):
    for k, v in req:
        Blogs.objects.update(k=v)


def delete(blog_id):
    Blogs.objects.filter(id=blog_id).delete()


def get():
    return to_blogs(Blogs.objects.all())


def get_details(blog_id):
    return to_blog(Blogs.objects.filter(id=blog_id).first())


def to_blog(blog):
    blog_arrange = {
        "id": blog.id,
        "title": blog.title,
        "content": blog.content,
        "author": blog.author,
        "create_time": blog.create_time,
        "lastmodified_time": blog.lastmodified_time
    }
    return blog_arrange


def to_blogs(blogs):
    out = []
    for blog in blogs:
        blog_arrange = {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "author": blog.author,
            "create_time": blog.create_time,
            "lastmodified_time": blog.lastmodified_time
        }
        out.append(blog_arrange)
    return out
