from tabnanny import verbose
from django.db import models
from helloworld.models import testimonial_admin,testimonial_user,testimonial_admin_french,testimonial_user_french
# Create your models here.

class Testimonial_Admin(testimonial_admin):
    class Meta:
        proxy = True
        verbose_name_plural ="Manage Testimonial (Admin)"

class Testimonial(testimonial_user):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Testimonial"

class Testimonial_Admin_french(testimonial_admin_french):
    class Meta:
        proxy = True
        verbose_name_plural ="Manage Testimonial (Admin) (French)"

class Testimonial_french(testimonial_user_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Testimonial (French)"