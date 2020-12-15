from django.shortcuts import render, redirect
from .models import *

def index(request):
    recent_posts = BlogPost.objects.all().order_by('created_at')[0:3]
    context={
        "all_blog_sections": BlogSection.objects.all(),
        "posts": recent_posts
    }
    return render(request, "index.html", context)

def blog(request):
    context={
        "all_blog_sections": BlogSection.objects.all(),
    }
    return render(request, "blog.html", context)

def view_blog_section(request, blog_section_id):
    context={
        "all_blog_sections": BlogSection.objects.all(),
        "blog_section": BlogSection.objects.get(id=blog_section_id)
    }
    return render(request, 'blog_section.html', context)

def view_blog_post(request, blog_section_id, blog_post_id):
    context={
        "all_blog_sections": BlogSection.objects.all(),
        "blog_section": BlogSection.objects.get(id=blog_section_id),
        "blog_post": BlogPost.objects.get(id=blog_post_id)
    }
    return render(request, 'blog_post.html', context)

def properties_preview(request):
    context={
        "all_blog_sections": BlogSection.objects.all(),
    }
    return render(request, 'properties.html', context)

def view_property1(request):
    context={
        "all_blog_sections": BlogSection.objects.all(),
    }
    return render(request, 'property_page1.html', context)

def view_property2(request):
    context={
        "all_blog_sections": BlogSection.objects.all(),
    }
    return render(request, 'property_page2.html', context)