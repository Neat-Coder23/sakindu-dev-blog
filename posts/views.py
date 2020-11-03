from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import PostForm,CommentsForm
from django.utils import timezone
from datetime import datetime

# Create your views here.
def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    commentcount = Comments.objects
    return render(request, 'posts_list.html', {'posts':posts, 'comments':commentcount})

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    
    form = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comments(
                pub_date=datetime.now(),
                author=form.cleaned_data["author"],
                comment=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            pri_key=post.pk
            return redirect(f'/posts/{pri_key}#comments')

    comments = Comments.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'form':form})

def post_new(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            newpost = postform.save(commit=False)
            newpost.save()
            return redirect('post_detail',pk=newpost.pk)
    else:
        postform = PostForm()
    return render(request, 'post_new.html',{'form':postform})




