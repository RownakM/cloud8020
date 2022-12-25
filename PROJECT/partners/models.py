from tabnanny import verbose
from django.db import models
from helloworld.models import p_artners,p_artners_french
from helloworld.models import Sub_Partners,Sub_Partners_french,part_text_french,part_text
# Create your models here.

class Partners(p_artners):
    class Meta:
        proxy = True
        verbose_name_plural="Manage Partner"

class Partner_Content(Sub_Partners):
    class Meta:
        proxy = True
        verbose_name_plural="Manage Partner Content"


class Partners_french(p_artners_french):
    class Meta:
        proxy = True
        verbose_name_plural="Manage Partner (French)"

class Partner_Content_french(Sub_Partners_french):
    class Meta:
        proxy = True
        verbose_name_plural="Manage Partner Content (French)"
class part_text1(part_text):
    class Meta:
        proxy = True
        verbose_name_plural='Manage Headers'
class part_text2(part_text_french):
    class Meta:
        proxy = True
        verbose_name_plural='Manage Headers (French)'
