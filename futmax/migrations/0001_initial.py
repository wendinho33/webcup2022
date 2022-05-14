# Generated by Django 4.0.4 on 2022-05-14 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FutUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('images', models.ImageField(upload_to='futimages/')),
                ('price', models.CharField(choices=[('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('STARTUP', 'STARTUP'), ('SUPREME', 'STARTUP')], default='BASIC', max_length=12)),
                ('payment', models.CharField(choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default='MONTHLY', max_length=7)),
                ('scripts', models.FileField(blank=True, null=True, upload_to='futfile')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
