# Generated by Django 2.2 on 2020-12-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobson_digs_app', '0002_blogpost_blog_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_post_img',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='blogsection',
            name='blog_sec_banner',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='blogsection',
            name='blog_sec_logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
