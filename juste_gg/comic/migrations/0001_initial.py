# Generated by Django 3.2.7 on 2021-09-25 03:26

import comic.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_dir', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='content.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modfied_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to=comic.models.get_series_path)),
                ('content', models.CharField(max_length=500)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent_series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comic.series')),
                ('tags', models.ManyToManyField(to='content.Keyword')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]