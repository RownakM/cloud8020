from tabnanny import verbose
from django.db import models
from helloworld.models import videogallery,videogallery_french
from helloworld.models import videodata,videodata_french
# Create your models here.

class video(videogallery):
    class Meta:
        proxy =  True
class video_data(videodata):

    class Meta:
        proxy = True
        verbose_name_plural = "Video Info"

class video_french(videogallery_french):
    class Meta:
        proxy =  True
        verbose_name_plural = "Video (French)"
class video_data_french(videodata_french):

    class Meta:
        proxy = True
        verbose_name_plural = "Video Info (French)"