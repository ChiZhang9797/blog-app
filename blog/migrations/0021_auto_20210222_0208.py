# Generated by Django 3.1.7 on 2021-02-22 02:08

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20210222_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.post_folder),
        ),
    ]
