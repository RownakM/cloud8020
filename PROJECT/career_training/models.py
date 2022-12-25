from tabnanny import verbose
from weakref import proxy
from django.db import models
from helloworld.models import career_header,career_header_french,career_data,career_data_french,career_sub_data,career_sub_data_french,career_training_form

class career_header1(career_header):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Header'

class career_header2(career_header_french):
    class Meta:
        proxy=True
        verbose_name_plural="Manage Header (French)"
class career_data1(career_data):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Content'
class career_data2(career_data_french):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Content (French)'
class career_sub1(career_sub_data):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Sub Content'
class career_sub2(career_sub_data_french):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Sub Content (French)'
class career_form(career_training_form):
    class Meta:
        proxy=True
        verbose_name_plural='Training Entries'