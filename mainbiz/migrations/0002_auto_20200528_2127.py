# Generated by Django 3.0.6 on 2020-05-28 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainbiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Achievement/%Y/%m/%d')),
                ('description', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='images/Portfolio/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='images/Services/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=256)),
                ('image', models.ImageField(upload_to='images/Testimonials/%Y/%m/%d')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
