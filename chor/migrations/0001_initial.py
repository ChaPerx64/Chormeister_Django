# Generated by Django 4.2.1 on 2023-05-22 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('chor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chor.chor')),
            ],
        ),
        migrations.CreateModel(
            name='SongPropertyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('chor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chor.chor')),
            ],
        ),
        migrations.CreateModel(
            name='SongPropertyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chor.song')),
                ('songpropertyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chor.songpropertyname')),
            ],
        ),
    ]
