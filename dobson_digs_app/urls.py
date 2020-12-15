from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog', views.blog),
    path(f'blog/section_<int:blog_section_id>', views.view_blog_section),
    path(f'blog/section_<int:blog_section_id>/post_<int:blog_post_id>', views.view_blog_post),
    path('properties', views.properties_preview),
    path('properties/fort_worth', views.view_property1),
    path('properties/lake_travis', views.view_property2),
]