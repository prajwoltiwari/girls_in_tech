# Generated by Django 2.1.5 on 2019-04-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190419_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='project_pics'),
        ),
    ]