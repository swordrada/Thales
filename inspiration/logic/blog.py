from inspiration.models import *
from django.db.models import F
from datetime import datetime


def create(req):
    Blogs.objects.create(title=req["title"], content=req["content"])


def update(req):
    for k, v in req:
        Blogs.objects.update(k=v)


def delete(blog_id):
    Blogs.objects.filter(id=blog_id).delete()


def get():
    return to_blogs(Blogs.objects.raw(get_blog_query()))


def get_details(blog_id):
    query = get_blog_query("AND t1.id={} LIMIT 1".format(blog_id))
    result = Blogs.objects.raw(query)
    blog = result[0]
    cmts = BlogComments.objects.filter(blog_id=blog.id)
    return to_blog(result, cmts)


def update_click_time(blog_id):
    blog = Blogs.objects.filter(id=blog_id).first()
    cnt = blog.click_time
    cnt += 1
    Blogs.objects.filter(id=blog_id).update(click_time=cnt)


def to_blog(blog, comments):
    blog = blog[0]
    blog_arrange = {
        "id": blog.id,
        "title": blog.title,
        "content": blog.content,
        "user_id": blog.user_id,
        "username": blog.username,
        "role": blog.role,
        "click_time": blog.click_time,
        "create_time": datetime.strftime(blog.create_time, "%Y-%m-%d %H:%M:%S"),
        "lastmodified_time": datetime.strftime(blog.lastmodified_time, "%Y-%m-%d %H:%M:%S"),
        "comments": []
    }
    for comment in comments:
        comment.create_time = datetime.strftime(comment.create_time, "%Y-%m-%d %H:%M:%S")
        comment.lastmodified_time = datetime.strftime(comment.lastmodified_time, "%Y-%m-%d %H:%M:%S")
        blog_arrange["comments"].append(comment)

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
            "click_time": blog.click_time,
            "create_time": datetime.strftime(blog.create_time, "%Y-%m-%d"),
            "lastmodified_time": datetime.strftime(blog.lastmodified_time, "%Y-%m-%d"),
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
    t1.lastmodified_time,
    t1.click_time
FROM 
    blogs t1
INNER JOIN
users t2
ON t1.user_id = t2.id
{}
"""
    return sql.format(where)
