from django.http import HttpResponse, JsonResponse
from . import errors


def success_response(data):
    success_map = {
        "errno": 0,
        "errmsg": "success",
        "data": data,
    }
    return JsonResponse(success_map)


def failure_response(errno, data):
    errmsg = errors.ERROR_MAP[errno]
    if errmsg == "":
        errmsg = errors.ERROR_MSG_INTERNAL_ERROR

    failure_map = {
        "errno": errno,
        "errmsg": errmsg,
        "data": data,
    }
    return JsonResponse(failure_map)
