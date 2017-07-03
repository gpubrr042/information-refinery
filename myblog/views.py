
from django.shortcuts import render, get_object_or_404

from .models import Post




# Create your views here.

def post_list(request):
	queryset1 = Post.objects.all()
	context = {
	   "posts": queryset1
	}
	return render(request, 'myblog/post_list.html',context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})
