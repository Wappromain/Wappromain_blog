from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.
def index_page(request):
    posts = BlogPost.objects.all()
    context = {"posts" : posts}
    return render(request, 'blog/index.html', context)
