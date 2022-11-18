from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", hp_controller, name="hp"),
    path("more", learn_more_controller, name="more"),
    path("contact", contact_controller, name="contact"),
    path("podcast", podcast_contact_controller, name="podcast_contact"),
    path("blog/search", search_blog_controller, name="search_blog"),
    path("blog/get/<int:blog_id>", details_blog_controller, name="details_blog")
]
