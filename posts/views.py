from django.shortcuts import render, get_object_or_404

from posts.models import Group, Post

POSTS_PER_PAGE = 10


def index(request):
    latest = Post.objects.select_related('group')[:POSTS_PER_PAGE]
    return render(request, 'posts/index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group.objects.prefetch_related('posts'), slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
