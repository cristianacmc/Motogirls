from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import Postform
from django.shortcuts import redirect



def post_list(request):
    posts = Post.objects.order_by('categoria')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = Postform
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('blog/post_edit.html', {'form': form})
    else:
        form = Postform(instance=post)
    return render(request,'blog/post_edit.html', {'form': form})
