# Generated by Django 3.2.7 on 2021-09-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='content.Keyword'),
        ),
    ]
