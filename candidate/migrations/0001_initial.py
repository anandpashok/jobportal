# Generated by Django 4.0.4 on 2022-09-15 06:22

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
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='candprofile')),
                ('resume', models.FileField(null=True, upload_to='cvs')),
                ('qualification', models.CharField(max_length=120)),
                ('skills', models.CharField(max_length=120)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
