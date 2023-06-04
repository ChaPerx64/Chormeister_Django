# Generated by Django 4.2.1 on 2023-06-04 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userchorrole_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chor', '0005_alter_chor_created_by_alter_chor_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chor',
            name='participants',
            field=models.ManyToManyField(through='user.UserChorRole', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chor',
            name='owner',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chor_owned', to=settings.AUTH_USER_MODEL),
        ),
    ]
