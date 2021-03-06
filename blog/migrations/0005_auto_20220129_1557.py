# Generated by Django 3.0 on 2022-01-29 14:57

from django.db import migrations, models
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220124_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='blog/default_blog_thumbnail.jpg', force_format=None, keep_meta=True, quality=75, size=[400, 500], upload_to='blog/'),
        ),
    ]
