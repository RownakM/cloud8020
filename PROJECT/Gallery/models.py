from sre_parse import Verbose
from django.db import models
from helloworld.models import gallery_pic,gallery_pic_french
# Create your models here.

class Gallery(gallery_pic):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Gallery"

class Gallery_french(gallery_pic_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Gallery (French)"
