from django.shortcuts import render
from post.models import Post
from tag.models import Tag
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# Create your views here.

def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    query = tag.tag_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(query, 2)
    all_blogs = Post.objects.order_by('-created_date')[:5]
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')

    context = {
        "blogs": blogs,
        "tags": tags,
        "all_blogs": all_blogs
    }
    return render(request, 'category_blogs.html', context)
