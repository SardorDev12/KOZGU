# Generated by Django 5.1.3 on 2024-11-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_title'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag_id',
            field=models.ManyToManyField(blank=True, related_name='posts', to='tags.tag'),
        ),
    ]
