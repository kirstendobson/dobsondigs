# Generated by Django 2.2 on 2020-12-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobson_digs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_post_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]