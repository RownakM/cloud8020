from tabnanny import verbose
from weakref import proxy
from django.db import models
from helloworld.models import corpo_header,corpo_header_french,corpo_data,corpo_data_french,corpo_sub_data,corpo_sub_data_french

class corpo_header1(corpo_header):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Header'

class corpo_header2(corpo_header_french):
    class Meta:
        proxy=True
        verbose_name_plural="Manage Header (French)"
class corpo_data1(corpo_data):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Content'
class corpo_data2(corpo_data_french):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Content (French)'
class corpo_sub1(corpo_sub_data):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Sub Content'
class corpo_sub2(corpo_sub_data_french):
    class Meta:
        proxy=True
        verbose_name_plural='Manage Sub Content (French)'