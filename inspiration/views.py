from django.conf import settings
from django.http import HttpResponse
from django.template import loader

from inspiration.common import constant
from inspiration.utils.common import *
from inspiration.plugins.plugin_redis import RedisClient
from inspiration.logic.blog import *


# Main index show & render
def hp_controller(request):
    r = RedisClient()
    r.incrby(constant.VISIT_CALCULATOR_KEY, 1)

    tpl = loader.get_template('index.html')
    return HttpResponse(tpl.render(build_context(), request))


# Learn more index show & render
def learn_more_controller(request):
    tpl = loader.get_template('learnmore.html')
    r = RedisClient()
    result = r.get(constant.VISIT_CALCULATOR_KEY)
    context = {"calculate_result": result}
    return HttpResponse(tpl.render(merge_context(build_context(), context), request))


# Contact with me
def contact_controller(request):
    tpl = loader.get_template('contact.html')
    return HttpResponse(tpl.render(build_context(), request))


# podcast
def podcast_contact_controller(request):
    tpl = loader.get_template('podcast_contact.html')
    return HttpResponse(tpl.render(build_context(), request))


# Blog query page
def search_blog_controller(request):
    tpl = loader.get_template('blog.html')
    context = {
        "blog_list": get()
    }
    return HttpResponse(tpl.render(merge_context(build_context(), context), request))


def details_blog_controller(request, blog_id):
    tpl = loader.get_template('blog_details.html')
    context = {
        "blog": get_details(blog_id)
    }
    return HttpResponse(tpl.render(merge_context(build_context(), context), request))


def create_blog_controller(request):
    tpl = loader.get_template('blog.html')
    req = {
        "title": request.POST["title"],
        "author": request.POST["author"],
        "content": request.POST["content"]
    }
    create(req)
    return HttpResponse(tpl.render(build_context(), request))
