from django.shortcuts import render, get_object_or_404

from datetime import date

from .models import Post

def get_post_date(all_posts):
    return all_posts["date"]

def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    undefine_post = get_object_or_404(Post, slug=slug)
    # undefine_post = next(post for post in all_posts if post["slug"] == slug) 
    return render(request, "blog/post-detail.html", {
        "post": undefine_post,
        "post_tags": undefine_post.tags.all()
    })
