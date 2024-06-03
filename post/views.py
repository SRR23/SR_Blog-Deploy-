from django.shortcuts import render
from post.models import Post
from tag.models import Tag
from category.models import Category
from review.models import Review
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .forms import TextForm
from django.db.models import Q
# Create your views here.

def home(request):
    blogs=Post.objects.order_by('-created_date')
    tags=Tag.objects.order_by('-created_date')
    context={"blogs":blogs, "tags":tags}
    return render(request, 'home.html', context)

def blogs(request):
    query=Post.objects.order_by('-created_date')
    tags=Tag.objects.order_by('-created_date')
    page=request.GET.get('page', 1)
    paginator=Paginator(query,2)
    
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs=paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
        return redirect('blogs')
        
    context={"blogs":blogs, "tags":tags, "paginator":paginator}
    return render(request, 'blogs.html', context)


def blog_details(request, slug):
    form=TextForm()
    blog = get_object_or_404(Post, slug=slug)
    category = Category.objects.get(id=blog.category.id)
    related_blogs = category.category_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    favourite_by=request.user in blog.favourite.all()
    
    
    if request.method == "POST" and request.user.is_authenticated:
        form = TextForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            comment = form.cleaned_data.get('text')
            Review.objects.create(
                user=request.user,
                blog=blog,
                comment=comment,
                rating=rating,
            )
            
            return redirect('blog_details', slug=slug)

    context = {
        "blog": blog,
        "related_blogs": related_blogs,
        "tags": tags,
        "form":form,
        "favourite_by":favourite_by
    }
    return render(request, 'blog_details.html', context)


def search_blogs(request):
    search_key = request.GET.get('search', None)
    recent_blogs = Post.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    
    if search_key:
        blogs = Post.objects.filter(
            Q(title__icontains=search_key) |
            Q(category__title__icontains=search_key) |
            Q(user__username__icontains=search_key) |
            Q(tags__title__icontains=search_key)
        ).distinct()

        context = {
            "blogs": blogs,
            "recent_blogs": recent_blogs,
            "tags": tags,
            "search_key": search_key
        }

        return render(request, 'search_blogs.html', context)

    else:
        return redirect('home')
