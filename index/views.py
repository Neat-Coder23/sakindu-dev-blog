from django.shortcuts import render
from portfolioapp.models import Projects
from posts.models import Post
from django.utils import timezone
from random import randint

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    recent_posts = posts[:6]
    projects = Projects.objects.all()
    some_projects = projects[:10]
    number = randint(1,3)
    r_posts = posts[::number]
    r_projects = projects[::number]
    post_count = len(r_posts)
    post_count_list = []
    i = 0
    while i < post_count:
        post_count_list.append(i)
        i += 1
        if i == post_count:
            break;
    context = {
        'posts':recent_posts,
        'projects':some_projects,
        'r_posts':r_posts,
        'r_projects':r_projects,
        'indexes':post_count_list,
    }
    return render(request, 'main.html', context)
