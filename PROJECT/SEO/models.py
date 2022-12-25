from django.db import models
from helloworld.models import manageseo,manageseo_french
# Create your models here.
class manageseoproxy(manageseo):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage SEO Keywords"

class manageseoproxy_french(manageseo_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage SEO Keywords (French)"