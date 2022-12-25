from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from helloworld.models import slider_image
from helloworld.models import hero_text
from helloworld.models import brand_text
from helloworld.models import aboutus
from helloworld.models import solutions
from helloworld.models import Sub_Solutions
from helloworld.models import gallery_pic
from helloworld.models import whatwedo
def index(request):
    dests = slider_image.objects.all()
    slider_text=hero_text.objects.all()
    brand1=brand_text.objects.all()
    whate_do=whatwedo.objects.all()
    return render(request,'index.html',{'dests' : dests , 'slider_text': slider_text, 'brand1': brand1,'whate_do': whate_do})

def about(request):
    dests = aboutus.objects.all()
    brand1=brand_text.objects.all()
    return render(request,'about.html', {'dests': dests,'brand1': brand1})
def services(request):
    brand1=brand_text.objects.all()
    return render(request,'services.html',{'brand1': brand1})
def gallery(request):
    brand1=brand_text.objects.all()
    gallery_data=gallery_pic.objects.values('Image_Tag').distinct()
    gallery_data_all=gallery_pic.objects.all()
    return render(request,'portfolio.html',{'brand1': brand1,"galleryobj":gallery_data,"gallery_all":gallery_data_all})
def solution(request):
    brand1=brand_text.objects.all()
    solution_data=solutions.objects.all()
    return render(request,'solutions.html',{'brand1': brand1,"solutions":solution_data})

def dynamic_lookup_view_solutions(request,name):
    brand1=brand_text.objects.all()
    obj = solutions.objects.get(Service_name=name)
    obj_all = solutions.objects.all()
    obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
    context={
        "object":obj,
        "brand1":brand1,
        "obj_all":obj_all,
        "obj_sub":obj_sub,
    }
    return render(request,"blog-single.html",context)

def dynamic_lookup_view_sub_solutions(request,name):
    brand1=brand_text.objects.all()
    obj = Sub_Solutions.objects.get(Service_name=name)
    # obj_all = solutions.objects.all()
    # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
    context={
        "object":obj,
        "brand1":brand1,
        # "obj_all":obj_all,
        # "obj_sub":obj_sub,
    }
    return render(request,"blog-single-1.html",context)

def contact(request):
    brand1=brand_text.objects.all()
    return render(request,'contact.html',{'brand1': brand1})
  