
import imp
from django.contrib import admin
# from .models import aboutus
from .models import hero_text
from .models import brand_text
# from .models import aboutus
# from .models import solutions
# from .models import Sub_Solutions
# from .models import gallery_pic
# from .models import testimonial_admin
# from .models import testimonial_user
# from .models import whatwedo
from SEO.models import manageseoproxy,manageseoproxy_french
from File.models import file
from VIDEO_GALLERY.models import video,video_french
from VIDEO_GALLERY.models import video_data,video_data_french
from home.models import Hero,Logo,Content,Hero_french,Logo_french,Content_french
# from opt.bitnami.projects.PROJECT.helloworld.views import job
# from partners.models import Partner_Content
from solutions.models import Solutions,SubSolutions,Solutions_french,SubSolutions_french
# Register your models here.
from About.models import About,About_french
from Gallery.models import Gallery,Gallery_french
from Testimonials.models import Testimonial_Admin,Testimonial,Testimonial_Admin_french,Testimonial_french
from partners.models import Partners,Partner_Content,Partner_Content_french,Partners_french,part_text1,part_text2
from contact.models import Address,Email,Phone,Address_french,Email_french,Phone_french,contact_da
from helloworld.models import sol_text,sol_text_french,part_text,part_text_french,jobs,contact_info,projects_data,project_header,corpo_header_french,corpo_data,corpo_data_french,corpo_header,corpo_sub_data,corpo_sub_data_french
from Corporate_Training.models import corpo_header1,corpo_header2,corpo_data1,corpo_data2,corpo_sub1,corpo_sub2
from career_training.models import career_header1,career_header2,career_data1,career_data2,career_sub1,career_sub2,career_form

from Project_Page.models import project_head1,project_head2,project_data1,project_data2
# from helloworld.models import navoptions,navoptions_french
# from helloworld.models import p_artners,Sub_Partners
# Register your models here.
class project_data_table(admin.ModelAdmin):
    list_display = ['project_name']
    search_fields = ['project_name']
admin.site.register(project_data1,project_data_table)
admin.site.register(project_data2,project_data_table)
class career_form_table(admin.ModelAdmin):
    list_display = ['Name','Email','Description','Mobile','amt','Submitted_on']
admin.site.register(career_form,career_form_table)
class project_header_table(admin.ModelAdmin):
    list_display = ['header','sub']

admin.site.register(project_head1,project_header_table)
admin.site.register(project_head2,project_header_table)
# admin.site.register(slider_image)
admin.site.register(hero_text)
admin.site.register(brand_text)
admin.site.register(corpo_data1)
admin.site.register(corpo_data2)
admin.site.register(corpo_header1)
admin.site.register(corpo_header2)
admin.site.register(corpo_sub1)
admin.site.register(corpo_sub2)


admin.site.register(career_data1)
admin.site.register(career_data2)
admin.site.register(career_header1)
admin.site.register(career_header2)
admin.site.register(career_sub1)
admin.site.register(career_sub2)
# admin.site.register(aboutus)
# admin.site.register(solutions)
# admin.site.register(Sub_Solutions)
# admin.site.register(gallery_pic)
# admin.site.register(testimonial_user)
# admin.site.register(testimonial_admin)
class contact_display(admin.ModelAdmin):
    list_display=['Name','Email','Subject','Mess']
    search_fields=['Email']
# admin.site.register(whatwedo)
admin.site.register(contact_info,contact_display)
from django.utils.html import mark_safe
class Filter_Solutions(admin.ModelAdmin):
    list_display = ("Service_Name","Description","Text","link")
    search_fields = ['Service_name']
    def Service_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    def Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_subtext)
        )
    def link(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
            '<a href="../../../../media/%s">Click Here</a>' % (obj.Service_img)
        )

class Filter_Solutions_french(admin.ModelAdmin):
    list_display = ("Service_Name","Description","Text","link")
    search_fields = ['Service_name']
    def Service_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    def Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_subtext)
        )
    def link(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
            '<a href="../../../../media/%s">View</a>' % (obj.Service_img)
        )
class Filter_subSolutions(admin.ModelAdmin):
    list_display = ("Solution_Name","Description","Icon_Info","Icon_Set_1","Icon_Set_1_Text","Icon_Set_2","Icon_Set_2_Text","Icon_Set_3","Icon_Set_3_Text","Icon_Set_4","Icon_Set_4_Text")
    search_fields = ['Service_name']
    def Solution_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    # def Text(self, obj):
    #     # return HTML link that will not be escaped
    #     return mark_safe(
    #          (obj.Service_subtext)
    #     )
    def Icon_Info(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Info_Text)
        )
    def Icon_Set_1(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set1)
        )
    def Icon_Set_1_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set1_text)
        )

    def Icon_Set_2(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set2)
        )
    def Icon_Set_2_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set2_text)
        )
    def Icon_Set_3(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set3)
        )
    def Icon_Set_3_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set3_text)
        )
    def Icon_Set_4(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set4)
        )
    def Icon_Set_4_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Icon_set4_text)
        )
    
class Filter_subSolutions_french(admin.ModelAdmin):
    list_display = ("Solution_Name","Description","Linked_To")
    search_fields = ['Service_name']
    def Solution_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    # def Text(self, obj):
    #     # return HTML link that will not be escaped
    #     return mark_safe(
    #          (obj.Service_subtext)
    #     )
    def Linked_To(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Main_Service)
        )

class Filter_Partner(admin.ModelAdmin):
    list_display = ("Service_Name","Description","Text","Link")
    search_fields = ['Service_name']
    def Service_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    def Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_subtext)
        )
    def Link(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
            '<a href="../../../../media/%s">View</a>' % (obj.Service_img)
        ) 

class Filter_Partner_content_french(admin.ModelAdmin):
    list_display = ("Sub_Partner_Name","Description","Text","Linked_To")
    search_fields = ['Service_name']
    def Sub_Partner_Name(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_name)
        )
    def Description(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_content)
        )
    def Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Service_subtext)
        )
    def Linked_To(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.Main_Service)
        )
class Filter_About(admin.ModelAdmin):
    list_display = ("Main_Text","Counter_1","Counter_1_Text","Counter_2","Counter_2_Text","Counter_3","Counter_3_Text","Counter_4","Counter_4_Text","Image")
    search_fields = ['abouttext']
    def Main_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.abouttext)
        )
    def Counter_1(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter1)
        )
    def Counter_2(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter2)
        )
    def Counter_3(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter3)
        )
    def Counter_4(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter4)
        )
    def Counter_1_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter1_name)
        )
    def Counter_2_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter2_name)
        )
    def Counter_3_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter3_name)
        )
    def Counter_4_Text(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
             (obj.counter4_name)
        )
    def Image(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
            '<a href="../../../../media/%s">View</a>' % (obj.img)
        )
    # list_filter = ("Service_name")
admin.site.register(manageseoproxy)
admin.site.register(manageseoproxy_french)
admin.site.register(file)
admin.site.register(video)
admin.site.register(video_french)
admin.site.register(video_data)
# admin.site.register(corpo_header1)
admin.site.register(Hero)
admin.site.register(Logo)
admin.site.register(Content)
admin.site.register(Solutions,Filter_Solutions)
admin.site.register(SubSolutions,Filter_subSolutions)
admin.site.register(sol_text)
admin.site.register(sol_text_french)
admin.site.register(part_text1)
admin.site.register(part_text2)


admin.site.register(video_data_french)
admin.site.register(Hero_french)
admin.site.register(Logo_french)
admin.site.register(Content_french)
admin.site.register(Solutions_french,Filter_Solutions_french)
admin.site.register(SubSolutions_french,Filter_subSolutions_french)

admin.site.register(About,Filter_About)
admin.site.register(About_french,Filter_About)
admin.site.register(Gallery)
admin.site.register(Testimonial_Admin)
admin.site.register(Testimonial)
admin.site.register(Partners,Filter_Partner)
# admin.site.register(p_artners)

admin.site.register(Partner_Content,Filter_Partner_content_french)

class Address_setting(admin.ModelAdmin):
    search_fields = ['Address']

class Email_setting(admin.ModelAdmin):
    search_fields = ['E_mail']
admin.site.register(Address,Address_setting)
class contact_table(admin.ModelAdmin):
    list_display=['Name','Email','Subject','Mess','submitted_at']
    search_fields=['Email']
admin.site.register(contact_da,contact_table)
admin.site.register(Email,Email_setting)
admin.site.register(Phone)


admin.site.register(Gallery_french)
admin.site.register(Testimonial_Admin_french)
admin.site.register(Testimonial_french)
admin.site.register(Partners_french,Filter_Partner)
# admin.site.register(p_artners)
admin.site.register(Partner_Content_french,Filter_Partner_content_french)
admin.site.register(Address_french,Address_setting)
admin.site.register(Email_french,Email_setting)
admin.site.register(Phone_french)
# admin.site.register(jobs)
# admin.site.register(navoptions)
# admin.site.register(navoptions_french)