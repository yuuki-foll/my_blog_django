# Generated by Django 3.2.9 on 2021-11-21 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blog_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='id',
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.SlugField(primary_key=True, serialize=False, unique=True),
        ),
    ]