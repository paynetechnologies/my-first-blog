from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def post_list(request):
    #posts = Post.objects.all()
    #me = User.objects.get(username='payne')
    #posts = Post.objects.create(author=me, title='Sundays News', text='News Flash')
    posts = Post.objects.all()
    #posts = Post.objects.order_by('created_date')
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})