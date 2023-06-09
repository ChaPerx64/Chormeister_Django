# Generated by Django 4.2.3 on 2023-07-06 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('chor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chor',
            name='participants',
            field=models.ManyToManyField(editable=False, through='user.UserChorRole', to=settings.AUTH_USER_MODEL),
        ),
    ]
