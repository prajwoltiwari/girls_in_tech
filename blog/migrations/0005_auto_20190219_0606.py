# Generated by Django 2.1.5 on 2019-02-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
