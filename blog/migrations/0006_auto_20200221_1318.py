# Generated by Django 3.0.3 on 2020-02-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=45),
        ),
    ]
