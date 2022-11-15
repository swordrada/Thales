from django.conf import settings
from django.http import HttpResponse
from django.template import loader

from .plugins.plugin_redis import RedisClient

from .common import constant


# Main index show & render
def hp_controller(request):
    r = RedisClient()
    r.incrby(constant.VISIT_CALCULATOR_KEY, 1)

    tpl = loader.get_template('index.html')
    return HttpResponse(tpl.render(settings.CONTEXT_RENDER_MAP, request))


# Learn more index show & render
def learn_more_controller(request):
    tpl = loader.get_template('learnmore.html')
    r = RedisClient()
    result = r.get(constant.VISIT_CALCULATOR_KEY)

    context = {
        "calculate_result": result,
        "navbars": settings.CONTEXT_RENDER_MAP["navbars"]
    }

    return HttpResponse(tpl.render(context, request))
