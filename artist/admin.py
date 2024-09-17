from django.contrib import admin
from . models import Music,Album,NewReleases

# Register your models here.
admin.site.register(Music)
admin.site.register(Album)
admin.site.register(NewReleases)
