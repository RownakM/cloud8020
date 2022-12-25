from tabnanny import verbose
from weakref import proxy
from django.db import models


# Create your models here.
from helloworld.models import hero_text,hero_text_french
from helloworld.models import brand_text,home_content,brand_text_french,home_content_french
class Hero(hero_text):
    class Meta:
        verbose_name_plural="Modify Hero"
        proxy = True

class Logo(brand_text):
    class Meta:
        verbose_name_plural="Modify Logo"
        proxy = True

class Content(home_content):
    class Meta:
        verbose_name_plural="Manage Home Page Content"
        proxy = True


class Hero_french(hero_text_french):
    class Meta:
        verbose_name_plural="Modify Hero (French)"
        proxy = True

class Logo_french(brand_text_french):
    class Meta:
        verbose_name_plural="Modify Logo (French)"
        proxy = True

class Content_french(home_content_french):
    class Meta:
        verbose_name_plural="Manage Home Page Content (French)"
        proxy = True