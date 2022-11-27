from inspiration.models import *
from django.db.models import F


def create(req):
    Blogs.objects.create(title=req["title"], content=req["content"], author=req["author"])


def update(req):
    for k, v in req:
        Blogs.objects.update(k=v)


def delete(blog_id):
    Blogs.objects.filter(id=blog_id).delete()


def get():
    return to_blogs(Blogs.objects.raw(get_blog_query()))


def get_details(blog_id):
    result = get_blog_query("AND t1.id={} LIMIT 1".format(blog_id))
    return to_blog(Blogs.objects.raw(result))


def to_blog(blog):
    blog = blog[0]
    blog_arrange = {
        "id": blog.id,
        "title": blog.title,
        "content": blog.content,
        "user_id": blog.user_id,
        "username": blog.username,
        "role": blog.role,
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
            "user_id": blog.user_id,
            "username": blog.username,
            "role": blog.role,
            "create_time": blog.create_time,
            "lastmodified_time": blog.lastmodified_time
        }
        out.append(blog_arrange)
    return out


def get_blog_query(where=""):
    sql = """
        SELECT 
            t1.id,
            t1.title,
            t1.content,
            t1.user_id,
            t2.username,
            t2.role,
            t1.create_time,
            t1.lastmodified_time
        FROM 
            blogs t1
        LEFT JOIN
        users t2
        ON t1.user_id = t2.id 
        {}
    """
    return sql.format(where)
