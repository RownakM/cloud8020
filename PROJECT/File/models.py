from django.db import models

# Create your models here.

from helloworld.models import fileproxy
# Create your models here.
class file(fileproxy):
    class Meta:
        proxy = True
        verbose_name_plural = "File Management"