from django.urls import path
from . import views


urlpatterns = [
    path("blog", views.post_index, name="post_index"),
    path("post_details/<int:post_id>/", views.post_details, name="post_details"),
    path("post_details/<int:post_id>/comment", views.post_comment, name="post_comment"),
    path("post_details/<int:post_id>/reply/<int:comment_id>",views.reply_comment,name="reply_comment"),
]
