# Generated by Django 5.1.3 on 2024-11-25 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_category_name'),
        ('posts', '0013_alter_post_article_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='Article', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='categories.category', to_field='name'),
            preserve_default=False,
        ),
    ]