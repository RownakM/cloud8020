from tabnanny import verbose
from django.db import models
from helloworld.models import solutions,Sub_Solutions,solutions_french,Sub_Solutions_french

# Create your models here.

class Solutions(solutions):
    class Meta:
        proxy = True
        verbose_name_plural="Create / Manage Solutions"

class SubSolutions(Sub_Solutions):
    class Meta:
        proxy = True
        verbose_name_plural="Create / Manage Sub Solutions"


class Solutions_french(solutions_french):
    class Meta:
        proxy = True
        verbose_name_plural="Create / Manage Solutions (French)"

class SubSolutions_french(Sub_Solutions_french):
    class Meta:
        proxy = True
        verbose_name_plural="Create / Manage Sub Solutions (French)"
