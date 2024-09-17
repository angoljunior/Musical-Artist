from django.db import models

# Create your models here.
class Album(models.Model):
    album = models.CharField(default=None, max_length=200, blank=True, null=True)

    def __str__(self):
        return self.album

	#@daverobb2011
    class Meta:
        verbose_name_plural = 'Album'


# ==================MODELS FOR  SONGS================
class Music(models.Model):
    song_title      = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    artist_name     = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    album_title     = models.ForeignKey(Album, on_delete=models.CASCADE ,default=None)
    song_image      = models.FileField(upload_to='media/uploads' ,default=None, blank=True, null=True)
    video           = models.FileField(upload_to='media/uploads' ,default=None, blank=True, null=True)
    spotify_link    = models.CharField(max_length=200, blank=True, null=True)
    soundcloud_link = models.CharField(max_length=600, blank=True, null=True)
    applemusic_link = models.CharField(max_length=600, blank=True, null=True)
    audiomack       = models.CharField(max_length=600, blank=True, null=True)
    tidal           = models.CharField(max_length=600, blank=True, null=True)
    youtube         = models.CharField(max_length=600, blank=True, null=True)
    date_added      = models.DateTimeField(auto_now=True , blank=True, null=True)

    def __str__(self):
        return self.song_title

	#@daverobb2011
    class Meta:
        verbose_name_plural = 'Music'


#============FOR VIDEO DISPLAY============
class NewReleases(models.Model):
    song_title      = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    artist_name     = models.CharField(max_length=200 ,default=None, blank=True, null=True)
    album_title     = models.ForeignKey(Album, on_delete=models.CASCADE ,default=None)
    song_image      = models.FileField(upload_to='media/uploads' ,default=None, blank=True, null=True)
    song_video      = models.FileField(upload_to='media/uploads' ,default=None, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'NewReleases'





