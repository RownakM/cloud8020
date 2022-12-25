from tabnanny import verbose
from weakref import proxy
from django.db import models
from helloworld.models import contactModel_Address,contactModel_Phone,contactModel_Email,contactModel_Address_french,contactModel_Email_french,contactModel_Phone_french,contact_info
# Create your models here.

class Address(contactModel_Address):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Addresses"
class Email(contactModel_Email):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Emails"
class Phone(contactModel_Phone):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Phones"

class contact_da(contact_info):
    class Meta:
        proxy=True
        verbose_name_plural='Contact Form Data'


class Address_french(contactModel_Address_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Addresses (French)"
class Email_french(contactModel_Email_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Emails (French)"
class Phone_french(contactModel_Phone_french):
    class Meta:
        proxy = True
        verbose_name_plural = "Manage Phones (French)"

