from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Post, Comment, Reply

# Create your views here.

per_page = 2


def post_index(request):
    post_list = Post.objects.all().order_by("-created_on")
    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get("page")
    if page_number is None:
        page_number = 1
    posts = paginator.get_page(page_number)
    context = {"posts": posts}
    return render(request, "blog_app/blog.html", context)


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    posts = Post.objects.all().order_by("-created_on")
    comments = Comment.objects.all().filter(post_id=post_id).order_by("-created_on")
    context = {"post": post, "comments": comments, "posts": posts}
    return render(request, "blog_app/detail.html", context)


def post_comment(request, post_id):
    if request.method == "POST":
        posted_by = request.POST["name"]
        comment_desc = request.POST["comment"]
        commenter_email = request.POST["email"]
        commenter_website = request.POST["website"]
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment(
            posted_by=posted_by,
            comment_desc=comment_desc,
            commenter_email=commenter_email,
            commenter_website=commenter_website,
            post=post,
        )
        comment.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def reply_comment(request, post_id, comment_id):
    if request.method == "POST":
        replied_by = request.POST["reply_name"]
        reply_desc = request.POST["reply_comment"]
        comment = get_object_or_404(Comment, pk=comment_id)
        reply = Reply(comment=comment, replied_by=replied_by, reply_desc=reply_desc)
        reply.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
