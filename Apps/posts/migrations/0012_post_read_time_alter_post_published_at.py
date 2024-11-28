# Generated by Django 5.1.3 on 2024-11-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_article_pic_post_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.CharField(default='3 min', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]