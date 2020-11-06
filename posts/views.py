from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import PostForm,CommentsForm
from django.utils import timezone
from datetime import datetime
from django.conf import settings 
from django.core import mail 
from django.template.loader import render_to_string
from django.utils.html import strip_tags

i=False
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
            if form.cleaned_data["email"] == 'dehipitiya@gmail.com' or form.cleaned_data["email"] == 'sakindu.app@gmail.com':
                if request.user.is_authenticated == True:
                    i=True
                else:
                    i=False
            else:
                i=False
            comment = Comments(
                pub_date=datetime.now(),
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                comment=form.cleaned_data["body"],
                post=post,
                moderator=i
            )
            comment.save()
            pri_key=post.pk
            if request.user.is_authenticated != True:
                date = comment.pub_date
                context = {
                    'title':post.title,
                    'author':form.cleaned_data["author"],
                    'email':form.cleaned_data["email"],
                    'time':date,
                    'pri_key':pri_key,
                }
                subject = f'New Comment On {post.title}'
                html_message = render_to_string('mail_template.html', context=context)
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to = 'dehipitiya@gmail.com'

                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message) 
                
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




