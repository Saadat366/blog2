# Generated by Django 3.0.6 on 2020-06-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200609_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='author_photo'),
        ),
    ]
