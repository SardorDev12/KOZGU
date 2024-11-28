# Generated by Django 5.1.3 on 2024-11-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_post_category'),
        ('tags', '0005_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(default='New', related_name='posts', to='tags.tag'),
        ),
    ]