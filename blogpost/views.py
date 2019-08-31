#Django
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

#Blogpost
from .models import Post

#Post List#
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blogpost/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogpost/post_detail.html', {'post':post})
