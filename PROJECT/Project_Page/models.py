from sre_parse import Verbose
from tabnanny import verbose

from django.db import models

# Create your models here.
from helloworld.models import project_header,project_header_french,projects_data,projects_data_french

class project_head1(project_header):
    class Meta:
        proxy = True
        verbose_name_plural='Manage Project Header'
class project_head2(project_header_french):
    class Meta:
        proxy = True
        verbose_name_plural='Manage Project Header (French)'
class project_data1(projects_data):
    class Meta:
        proxy = True
        verbose_name_plural = 'Manage Project Content'
class project_data2(projects_data_french):
    class Meta:
        proxy = True
        verbose_name_plural='Manage Project Content (French)'


