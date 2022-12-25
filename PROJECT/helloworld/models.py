from contextlib import nullcontext
from distutils.command.upload import upload
from pyexpat import model
from random import choice, choices
from statistics import mode
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.db.models.fields import TextField
from tinymce.models import HTMLField
import os
import sys

class project_header(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')
class project_header_french(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')
class projects_data(models.Model):
    img=models.ImageField(upload_to='media',verbose_name='Image')
    project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Project Description')
    is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    Url=models.CharField(max_length=300,blank=True)
class projects_data_french(models.Model):
    img=models.ImageField(upload_to='media',verbose_name='Image')
    project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Project Description')
    is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    Url=models.CharField(max_length=300,blank=True)
    

class corpo_header(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')
class corpo_header_french(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')
class corpo_data(models.Model):
    # img=models.ImageField(upload_to='media',verbose_name='Image')
    # project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Page Content')
    # is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    # Url=models.CharField(max_length=300,blank=True)
class corpo_data_french(models.Model):
    # img=models.ImageField(upload_to='media',verbose_name='Image')
    # project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Page Content')
    # is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    # Url=models.CharField(max_length=300,blank=True)
# Create your models here.

class corpo_sub_data(models.Model):
    Sub_Corp_Name=models.CharField(max_length=200,verbose_name='Sub Corporate Name')
    Sub_Corp_Data=HTMLField(verbose_name='Content')
    Sub_tag=models.CharField(max_length=100)
class corpo_sub_data_french(models.Model):
    Sub_Corp_Name=models.CharField(max_length=200,verbose_name='Sub Corporate Name')
    Sub_Corp_Data=HTMLField(verbose_name='Content')
    Sub_tag=models.CharField(max_length=100)
class slider_image(models.Model):
    name = models.CharField(max_length=200,verbose_name = "Name")
    img = models.ImageField(upload_to='media',verbose_name = "Image")
    status = models.BooleanField(default=False,verbose_name = "Active")

    def __str__(self):
        # name1=self.name
        # new_string = name1.replace("_", " ")
        return self.name

    class Meta:
        verbose_name_plural = "Slider Image"

class slider_image_french(models.Model):
    name = models.CharField(max_length=200,verbose_name = "Name")
    img = models.ImageField(upload_to='media',verbose_name = "Image")
    status = models.BooleanField(default=False,verbose_name = "Active")

    def __str__(self):
        # name1=self.name
        # new_string = name1.replace("_", " ")
        return self.name

    class Meta:
        verbose_name_plural = "Slider Image"


class hero_text(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")

    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Hero Text"
class hero_text_french(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Hero Text"


class sol_text(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Solution Headers"
class sol_text_french(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Solution Headers(French)"

class part_text(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Partners Headers"
        
class part_text_french(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Main Text")
    subtext=models.CharField(max_length=200,verbose_name = "Sub Text")
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Partners Headers(French)"

class home_content(models.Model):
    content=HTMLField(verbose_name="Edit Home Page Content",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
class home_content_french(models.Model):
    content=HTMLField(verbose_name="Edit Home Page Content",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
class brand_text(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Company Name")
    img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Brand Text"

class brand_text_french(models.Model):
    text=models.CharField(max_length=300,verbose_name = "Company Name")
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "Brand Text"
class aboutus(models.Model):
    img = models.ImageField(upload_to='media',verbose_name = "Upload Image")
    abouttext=HTMLField(verbose_name = "About Us Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    counter1=models.IntegerField(verbose_name = "Counter Field 1")
    counter1_name=models.CharField(max_length=50,verbose_name = "Counter 1 Text")


    counter2=models.IntegerField(verbose_name = "Counter Field 2")
    counter2_name=models.CharField(max_length=50,verbose_name = "Counter 2 Text")


    counter3=models.IntegerField(verbose_name = "Counter Field 3")
    counter3_name=models.CharField(max_length=50,verbose_name = "Counter 3 Text")


    counter4=models.IntegerField(verbose_name = "Counter Field 4")
    counter4_name=models.CharField(max_length=50,verbose_name = "Counter 4 Text")

    def __str__(self):
        return self.abouttext
    class Meta:
        verbose_name_plural = "About Us"

class aboutus_french(models.Model):
    img = models.ImageField(upload_to='media',verbose_name = "Upload Image")
    abouttext=HTMLField(verbose_name = "About Us Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    counter1=models.IntegerField(verbose_name = "Counter Field 1")
    counter1_name=models.CharField(max_length=50,verbose_name = "Counter 1 Text")


    counter2=models.IntegerField(verbose_name = "Counter Field 2")
    counter2_name=models.CharField(max_length=50,verbose_name = "Counter 2 Text")


    counter3=models.IntegerField(verbose_name = "Counter Field 3")
    counter3_name=models.CharField(max_length=50,verbose_name = "Counter 3 Text")


    counter4=models.IntegerField(verbose_name = "Counter Field 4")
    counter4_name=models.CharField(max_length=50,verbose_name = "Counter 4 Text")

    def __str__(self):
        return self.abouttext
    class Meta:
        verbose_name_plural = "About Us"

class solutions(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Service Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Index Page Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_img=models.ImageField(upload_to='media',verbose_name = "Upload Image")
    Service_icon=models.CharField(max_length=100,verbose_name="Choose Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    tag=models.CharField(max_length=100,verbose_name='Tag')
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Solutions"
class solutions_french(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Service Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Index Page Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_img=models.ImageField(upload_to='media',verbose_name = "Upload Image")
    tag=models.CharField(max_length=100,verbose_name='Tag')

    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Solutions"
class Sub_Solutions(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Solution Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    # Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")


    Main_Service=models.CharField(max_length=200,verbose_name = "Main Service Name (Case Sensitive)")

    Info_Text=HTMLField()
    tag=models.CharField(max_length=100,verbose_name='Tag')


    Icon_set1=models.CharField(max_length=100,verbose_name="Icon 1",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set1_text=HTMLField(verbose_name="Icon 1 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set2=models.CharField(max_length=100,verbose_name="Icon 2",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set2_text=HTMLField(verbose_name="Icon 2 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set3=models.CharField(max_length=100,verbose_name="Icon 3",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set3_text=HTMLField(verbose_name="Icon 3 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set4=models.CharField(max_length=100,verbose_name="Icon 4",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>",blank=True)
    Icon_set4_text=HTMLField(verbose_name="Icon 4 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.",blank=True)
    # Service_img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Sub Solutions"

class Sub_Solutions_french(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Solution Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Main_Service=models.CharField(max_length=200,verbose_name = "Main Service Name (Case Sensitive)")
    Service_name_english=models.CharField(max_length=300,verbose_name='Service Name (English)')

    Info_Text=HTMLField()
    tag=models.CharField(max_length=100,verbose_name='Tag')


    Icon_set1=models.CharField(max_length=100,verbose_name="Icon 1",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set1_text=HTMLField(verbose_name="Icon 1 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set2=models.CharField(max_length=100,verbose_name="Icon 2",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set2_text=HTMLField(verbose_name="Icon 2 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set3=models.CharField(max_length=100,verbose_name="Icon 3",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set3_text=HTMLField(verbose_name="Icon 3 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set4=models.CharField(max_length=100,verbose_name="Icon 4",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set4_text=HTMLField(verbose_name="Icon 4 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    # Service_img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Sub Solutions"


class Sub_Partners(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Solution Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Main_Service=models.CharField(max_length=200,verbose_name = "Main Service Name (Case Sensitive)")

    Info_Text=HTMLField()


    Icon_set1=models.CharField(max_length=100,verbose_name="Icon 1",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set1_text=HTMLField(verbose_name="Icon 1 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set2=models.CharField(max_length=100,verbose_name="Icon 2",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set2_text=HTMLField(verbose_name="Icon 2 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set3=models.CharField(max_length=100,verbose_name="Icon 3",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set3_text=HTMLField(verbose_name="Icon 3 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set4=models.CharField(max_length=100,verbose_name="Icon 4",blank=True,help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set4_text=HTMLField(verbose_name="Icon 4 Text",blank=True,help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    # Service_img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Sub Partners"

class Sub_Partners_french(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Solution Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Main_Service=models.CharField(max_length=200,verbose_name = "Main Service Name (Case Sensitive)")

    Info_Text=HTMLField()


    Icon_set1=models.CharField(max_length=100,verbose_name="Icon 1",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set1_text=HTMLField(verbose_name="Icon 1 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set2=models.CharField(max_length=100,verbose_name="Icon 2",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set2_text=HTMLField(verbose_name="Icon 2 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set3=models.CharField(max_length=100,verbose_name="Icon 3",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set3_text=HTMLField(verbose_name="Icon 3 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    Icon_set4=models.CharField(max_length=100,verbose_name="Icon 4",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_set4_text=HTMLField(verbose_name="Icon 4 Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    # Service_img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Sub Partners"



class gallery_pic(models.Model):
    Image_Caption=HTMLField(verbose_name = "Image Caption",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Image_Tag=models.CharField(max_length=300,verbose_name = "Image Tag")
    # Service_subtext=HTMLField()
    # Main_Service=models.CharField(max_length=200)
    img=models.ImageField(upload_to='media',verbose_name = "Upload Image")

    def __str__(self):
        return self.Image_Caption
    class Meta:
        verbose_name_plural = "Gallery"

class gallery_pic_french(models.Model):
    Image_Caption=HTMLField(verbose_name = "Image Caption",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Image_Tag=models.CharField(max_length=300,verbose_name = "Image Tag")
    # Service_subtext=HTMLField()
    # Main_Service=models.CharField(max_length=200)
    img=models.ImageField(upload_to='media',verbose_name = "Upload Image")

    def __str__(self):
        return self.Image_Caption
    class Meta:
        verbose_name_plural = "Gallery"


class testimonial_user(models.Model):
    # Info_text=HTMLField()
    User_img=models.ImageField(upload_to='user',verbose_name = "Upload Image")
    user_name=models.CharField(max_length=200,verbose_name = "Name")
    user_designation=models.CharField(max_length=100,verbose_name = "Designation")
    user_review=HTMLField(verbose_name = "Review / What they Say",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    def __str__(self):
        return {{self.user_name|safe}}

    class Meta:
        verbose_name_plural = "Testimonials"
class testimonial_user_french(models.Model):
    # Info_text=HTMLField()
    User_img=models.ImageField(upload_to='user',verbose_name = "Upload Image")
    user_name=models.CharField(max_length=200,verbose_name = "Name")
    user_designation=models.CharField(max_length=100,verbose_name = "Designation")
    user_review=HTMLField(verbose_name = "Review / What they Say",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

    def __str__(self):
        return {{self.user_name|safe}}

    class Meta:
        verbose_name_plural = "Testimonials"
class testimonial_admin(models.Model):
    Info_text=HTMLField(verbose_name = "Change Intro Text on Testimonials",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    class Meta:
        verbose_name_plural = "Testimonial(Admin)"

class testimonial_admin_french(models.Model):
    Info_text=HTMLField(verbose_name = "Change Intro Text on Testimonials",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    class Meta:
        verbose_name_plural = "Testimonial(Admin)"

class whatwedo(models.Model):
    what_we_do_main=HTMLField(verbose_name="Main Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    what_we_do_sub=HTMLField(verbose_name="Short Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    def __str__(self):
        return self.what_we_do_main
    class Meta:
        verbose_name_plural = "What We Do"
class whatwedo_french(models.Model):
    what_we_do_main=HTMLField(verbose_name="Main Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    what_we_do_sub=HTMLField(verbose_name="Short Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    def __str__(self):
        return self.what_we_do_main
    class Meta:
        verbose_name_plural = "What We Do"

class manageseo(models.Model):
    keywords=models.CharField(max_length=300,verbose_name="Add Keywords")
    def __str__(self):
        return self.keywords
class manageseo_french(models.Model):
    keywords=models.CharField(max_length=300,verbose_name="Add Keywords")
    def __str__(self):
        return self.keywords

class fileproxy(models.Model):
    File_upload = models.FileField(upload_to='upload',verbose_name="Upload File")
    def __str__(self):
        return self.File_upload
class fileproxy_french(models.Model):
    File_upload = models.FileField(upload_to='upload',verbose_name="Upload File")
    def __str__(self):
        return self.File_upload

class videogallery(models.Model):
    Video_Gallery = models.CharField(max_length=300,verbose_name="Video URL")
    # Icon_Name=models.CharField(max_length=100,verbose_name="Set Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Video_Thumbnail=models.ImageField(upload_to='video_upload',verbose_name="Upload Video Thumbnail")
class videogallery_french(models.Model):
    Video_Gallery = models.CharField(max_length=300,verbose_name="Video URL")
    # Icon_Name=models.CharField(max_length=100,verbose_name="Set Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Video_Thumbnail=models.ImageField(upload_to='video_upload',verbose_name="Upload Video Thumbnail")

class videodata(models.Model):
    Icon_Name=models.CharField(max_length=100,verbose_name="Set Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_Text=HTMLField(verbose_name="Set Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Icon_subtext=HTMLField(verbose_name="Set Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
class videodata_french(models.Model):
    Icon_Name=models.CharField(max_length=100,verbose_name="Set Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    Icon_Text=HTMLField(verbose_name="Set Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Icon_subtext=HTMLField(verbose_name="Set Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")

class p_artners(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Partner Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_img=models.ImageField(upload_to='media',verbose_name = "Upload Image")
    Service_icon=models.CharField(max_length=100,verbose_name="Choose Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")

    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Partners"

class p_artners_french(models.Model):
    Service_name=models.CharField(max_length=300,verbose_name = "Partner Name")
    Service_content=HTMLField(verbose_name = "Description",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_subtext=HTMLField(verbose_name = "Sub Text",help_text="To Upload an Image , Host it on <a href='https://imgbb.com/' target='_blank'>imgbb.com</a> for free ! and paste the Share URL here.")
    Service_img=models.ImageField(upload_to='media',verbose_name = "Upload Image")
    Service_icon=models.CharField(max_length=100,verbose_name="Choose Icon",help_text="For complete cheatsheet of available icons , visit <a href='https://boxicons.com/cheatsheet' target='_blank'>Here</a>")
    def __str__(self):
        return self.Service_name
    class Meta:
        verbose_name_plural = "Partners"


class test(models.Model):
    ch=HTMLField()

class contactModel_Address(models.Model):
    Address=models.CharField(max_length=400,verbose_name="Address")
    def __str__(self):
        return self.Address
class contactModel_Address_french(models.Model):
    Address=models.CharField(max_length=400,verbose_name="Address")
    def __str__(self):
        return self.Address

class contactModel_Email(models.Model):
    E_mail=models.CharField(max_length=200,verbose_name="E-Mail")
    def __str__(self):
        return self.E_mail
class contactModel_Email_french(models.Model):
    E_mail=models.CharField(max_length=200,verbose_name="E-Mail")
    def __str__(self):
        return self.E_mail

class contactModel_Phone(models.Model):
    Phone=models.CharField(max_length=100,verbose_name="Mobile Number")
    def __str__(self):
        return self.Phone

class contactModel_Phone_french(models.Model):
    Phone=models.CharField(max_length=100,verbose_name="Mobile Number")
    def __str__(self):
        return self.Phone

class navoptions(models.Model):
    nText=models.CharField(max_length=100)
    nLink=models.CharField(max_length=100)

class navoptions_french(models.Model):
    nText=models.CharField(max_length=100)
    nLink=models.CharField(max_length=100)
class jobs(models.Model):
    Job_Title=models.CharField(max_length=200)
    Job_Type=models.CharField(max_length=200,choices=[('Full Time','Full Time'),('Permanent','Permanent'),('Part-Time','Part-Time'),('Contract','Contract'),('Temporary','Temporary'),('Casual','Casual'),('Apprenticeship','Apprenticeship'),('Internship','Internship'),('Freelance','Freelance')])
    category_list=[
        ('Job category','Job Category')
    ]
    Job_Category=models.CharField(max_length=300,choices=category_list)
    country_list=[('India','India')]
    State_List=[('Wb','Wb')]
    Country=models.CharField(max_length=300,choices=country_list)
    State=models.CharField(max_length=300,choices=State_List)
    Date=models.DateField()
    Job_Description=HTMLField()
    Brief_Descrition=HTMLField()
    Recruitment_From=models.CharField(max_length=300)

class contact_info(models.Model):
    Name=models.CharField(max_length=300)
    Email=models.EmailField()
    Subject=models.CharField(max_length=300)
    Mess=HTMLField()
    submitted_at=models.DateTimeField(auto_now_add=True)

class career_header(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')
class career_header_french(models.Model):
    header=models.CharField(max_length=200,verbose_name='Header Text')
    sub=models.CharField(max_length=100,verbose_name='Sub text')

class career_data(models.Model):
    # img=models.ImageField(upload_to='media',verbose_name='Image')
    # project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Page Content')
    # is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    # Url=models.CharField(max_length=300,blank=True)
class career_data_french(models.Model):
    # img=models.ImageField(upload_to='media',verbose_name='Image')
    # project_name=models.CharField(max_length=200,verbose_name='Project Name')
    project_desc=HTMLField(verbose_name='Page Content')
    # is_link=models.BooleanField(default=False,verbose_name='URL Active ?')
    # Url=models.CharField(max_length=300,blank=True)
# Create your models here.

class career_sub_data(models.Model):
    Sub_career_Name=models.CharField(max_length=200,verbose_name='Sub Corporate Name')
    Sub_career_Data=HTMLField(verbose_name='Content')
    Sub_tag=models.CharField(max_length=100)
    Sub_Start_Date=models.DateField(verbose_name='Start Date')
    Sub_End_Date=models.DateField(verbose_name='End Date')
    Fee=models.IntegerField(default=0)
class career_sub_data_french(models.Model):
    Sub_career_Name=models.CharField(max_length=200,verbose_name='Sub Corporate Name')
    Sub_career_Data=HTMLField(verbose_name='Content')
    Sub_tag=models.CharField(max_length=100)
    Sub_Start_Date=models.DateField(verbose_name='Start Date')
    Sub_End_Date=models.DateField(verbose_name='End Date')
    Fee=models.IntegerField(default=0)

class career_training_form(models.Model):
    Name=models.CharField(max_length=300,verbose_name='Name')
    Email=models.EmailField(max_length=200,verbose_name='Email')
    Description=models.CharField(max_length=300,verbose_name='Training Name')
    Mobile=models.IntegerField(verbose_name='Mobile')
    amt=models.IntegerField(verbose_name='Amount')
    Submitted_on=models.DateTimeField(auto_now_add=True)



