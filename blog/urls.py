from django.urls import path
from .views import start_page, posts, post_detail

urlpatterns = [
    path("", start_page, name="starting-page"),
    path("posts", posts, name="posts-page"),
    path("posts/<slug>", post_detail, name="post-details-page")
]
