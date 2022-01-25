# Generated by Django 4.0.1 on 2022-01-24 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], default='male', max_length=20)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('work', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.CharField(blank=True, max_length=800, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
