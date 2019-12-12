# Generated by Django 3.0 on 2019-12-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
