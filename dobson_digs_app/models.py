from django.db import models

class BlogSection(models.Model):
    name = models.CharField(max_length=45)
    desc = models.TextField()
    blog_sec_logo = models.ImageField(upload_to='media')
    blog_sec_banner = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=45)
    intro = models.TextField()
    blog_post_logo = models.ImageField(upload_to='media', null=True)
    blog_post_img = models.ImageField(upload_to='media', null=True)
    blog_section = models.ForeignKey(BlogSection, related_name="blog_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogPostSection(models.Model):
    subtitle = models.CharField(max_length=125)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, related_name="blog_post_sections", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
