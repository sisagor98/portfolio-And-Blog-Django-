from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from .models import Comment


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    contest = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", contest)


def blog_categories(request, category):
    post = Post.objects.filter(
        categories__name__contains= category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts" : post
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/blog_detail.html", context)