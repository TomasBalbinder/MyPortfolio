from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils.translation import ngettext

# Create your views here.
def all_blog(request):
    blog = Blog.objects.order_by('-date')[:]
    return render(request, 'blogApp/all_blog.html', {'blog' : blog})


def details(request, blog_id):

    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blogApp/details.html', {'detail_blog': detail_blog})




