# Generated by Django 3.0.6 on 2020-06-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbiz', '0020_auto_20200626_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/blog/%Y/%m/%d'),
        ),
    ]
