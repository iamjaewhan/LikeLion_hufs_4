# Generated by Django 3.2.5 on 2021-07-25 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_kor', models.CharField(max_length=50)),
                ('title_eng', models.CharField(max_length=50)),
                ('poster_url', models.CharField(max_length=300)),
                ('rating_aud', models.CharField(max_length=50)),
                ('rating_cri', models.CharField(max_length=50)),
                ('rating_net', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('showtimes', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('rate', models.CharField(max_length=50)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=300)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rate', models.IntegerField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
            ],
        ),
    ]
