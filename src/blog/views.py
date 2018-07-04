from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
<<<<<<< HEAD

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})
=======
>>>>>>> 4ab97f70d7c8e7293b154f071253dd012a952c09
