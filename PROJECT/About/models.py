from tabnanny import verbose
from django.db import models

# Create your models here.
from helloworld.models import aboutus,aboutus_french

class About(aboutus):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage About Us"
class About_french(aboutus_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage About Us(French)"