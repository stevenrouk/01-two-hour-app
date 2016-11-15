from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import NewPostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_post = Post(text=form.cleaned_data['text'], pub_date=timezone.now())
            new_post.save()

            return redirect('home')
    else:
        form = NewPostForm()

    return render(request, 'blog/add-post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post-detail.html', {'post': post})
