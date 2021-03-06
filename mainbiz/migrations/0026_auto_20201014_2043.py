# Generated by Django 3.0.6 on 2020-10-14 20:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainbiz', '0025_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tag')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='mainbiz.Tag'),
        ),
    ]
