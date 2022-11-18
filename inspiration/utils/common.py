import json

from django.conf import settings


def build_context():
    return {
        "navbars": settings.CONTEXT_RENDER_MAP["navbars"],
    }


def merge_context(dict1, dict2):
    dict2.update(dict1)
    return dict2
