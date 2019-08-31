#Django
from django.shortcuts import render
from django.utils import timezone

#Blogpost
from .models import Post

#Post List#
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blogpost/post_list.html', {'posts':posts})
