# Generated by Django 5.1.3 on 2024-11-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]