# Generated by Django 5.0.7 on 2024-09-14 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0010_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album_title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='artist.album'),
        ),
    ]