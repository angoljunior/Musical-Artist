# Generated by Django 5.0.7 on 2024-09-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_music_album_title_music_video_alter_music_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='song_title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
