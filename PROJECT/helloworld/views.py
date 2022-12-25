from django.shortcuts import render
from django.conf import settings
from googletrans import Translator
from django.utils.safestring import mark_safe
import json
from django.views.decorators.csrf import csrf_exempt


import urllib
# Create your views here.
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.db.models import Q
from helloworld.models import corpo_sub_data, corpo_sub_data_french, slider_image,slider_image_french,career_sub_data,career_sub_data_french
from helloworld.models import hero_text,hero_text_french
from helloworld.models import brand_text,brand_text_french
from helloworld.models import aboutus,aboutus_french
from helloworld.models import solutions,solutions_french
from helloworld.models import Sub_Solutions,Sub_Solutions_french
from helloworld.models import gallery_pic,gallery_pic_french
from helloworld.models import videodata,videodata_french
from helloworld.models import videogallery,videogallery_french
from helloworld.models import home_content,home_content_french
from helloworld.models import p_artners,p_artners_french
from helloworld.models import Sub_Partners,Sub_Partners_french
from helloworld.models import contactModel_Address,contactModel_Email,contactModel_Phone,contactModel_Address_french,contactModel_Email_french,contactModel_Phone_french,career_training_form
from helloworld.models import sol_text,sol_text_french,part_text,part_text_french,jobs
# from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from helloworld.models import contact_info,project_header,projects_data,project_header_french,projects_data_french,corpo_data,corpo_data_french,corpo_header,corpo_header_french,career_data,career_data_french,career_header,career_header_french

def job_search(request):
    cr=request.POST['search']
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        
        solution_data=jobs.objects.filter(Q(Job_Title=cr)|Q(Job_Type=cr))
        par_header=part_text.objects.all()

        return render(request,'job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=jobs.objects.filter(Q(Job_Title=cr)|Q(Job_Type=cr))
        par_header=part_text_french.objects.all()
        return render(request,'fr/job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=jobs.objects.filter(Q(Job_Title=cr)|Q(Job_Type=cr))
        par_header=part_text.objects.all()
        return render(request,'job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})


def job(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=jobs.objects.all()
        par_header=part_text.objects.all()
        return render(request,'job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=jobs.objects.all()
        par_header=part_text_french.objects.all()
        return render(request,'fr/job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=jobs.objects.all()
        par_header=part_text.objects.all()
        return render(request,'job.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})

def index(request):
    # request.session['lang']='fr'
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        content=home_content.objects.all()
        dests = slider_image.objects.all()
        slider_text=hero_text.objects.all()
        brand1=brand_text.objects.all()
        solution_data=solutions.objects.all()
        vdata=videodata.objects.all()
        vgall=videogallery.objects.all()
        
        l=['blue','pink','green']
        return render(request,'index.html',{'dests' : dests , 'slider_text': slider_text, 'brand1': brand1,'whatdo':solution_data,"l":l,"vdata":vdata,"vgall":vgall,'content':content,"lan":lan})
        
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        content=home_content_french.objects.all()
        dests = slider_image_french.objects.all()
        slider_text=hero_text_french.objects.all()
        brand1=brand_text_french.objects.all()
        solution_data=solutions_french.objects.all()
        vdata=videodata_french.objects.all()
        vgall=videogallery_french.objects.all()
        l=['blue','pink','green']
        return render(request,'fr/index.html',{'dests' : dests , 'slider_text': slider_text, 'brand1': brand1,'whatdo':solution_data,"l":l,"vdata":vdata,"vgall":vgall,'content':content,"lan":lan})
    else:
    # send_mail(
    #     'Subject',
    #     'Message',
    #     'tiulectures@gmail.com',
    #     ['rownakmazumder@gmail.com'],
    #     fail_silently=False
    # )
        lan=request.session['lang']
        content=home_content.objects.all()
        dests = slider_image.objects.all()
        slider_text=hero_text.objects.all()
        brand1=brand_text.objects.all()
        solution_data=solutions.objects.all()
        vdata=videodata.objects.all()
        vgall=videogallery.objects.all()
        l=['blue','pink','green']
        return render(request,'index.html',{'dests' : dests , 'slider_text': slider_text, 'brand1': brand1,'whatdo':solution_data,"l":l,"vdata":vdata,"vgall":vgall,'content':content,"lan":lan})

def about(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        dests = aboutus.objects.all()
        brand1=brand_text.objects.all()
        return render(request,'about.html', {'dests': dests,'brand1': brand1,"lan":lan})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        dests = aboutus_french.objects.all()
        brand1=brand_text_french.objects.all()
        return render(request,'fr/about.html', {'dests': dests,'brand1': brand1,"lan":lan})
    else:
        lan=request.session['lang']
        dests = aboutus.objects.all()
        brand1=brand_text.objects.all()
        return render(request,'about.html', {'dests': dests,'brand1': brand1,"lan":lan})
    
def services(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        return render(request,'services.html',{'brand1': brand1,"lan":lan})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        return render(request,'fr/services.html',{'brand1': brand1,"lan":lan})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        return render(request,'services.html',{'brand1': brand1,"lan":lan})
def gallery(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        gallery_data=gallery_pic.objects.values('Image_Tag').distinct()
        gallery_data_all=gallery_pic.objects.all()
        return render(request,'fr/portfolio.html',{'brand1': brand1,"galleryobj":gallery_data,"gallery_all":gallery_data_all,"lan":lan})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        gallery_data=gallery_pic_french.objects.values('Image_Tag').distinct()
        gallery_data_all=gallery_pic_french.objects.all()
        return render(request,'fr/portfolio.html',{'brand1': brand1,"galleryobj":gallery_data,"gallery_all":gallery_data_all,"lan":lan})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        gallery_data=gallery_pic.objects.values('Image_Tag').distinct()
        gallery_data_all=gallery_pic.objects.all()
        return render(request,'portfolio.html',{'brand1': brand1,"galleryobj":gallery_data,"gallery_all":gallery_data_all,"lan":lan})
def solution(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=solutions.objects.all()
        sol_header=sol_text.objects.all()
        return render(request,'solutions.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=solutions_french.objects.all()
        sol_header=sol_text_french.objects.all()
        return render(request,'fr/solutions.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})

    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=solutions.objects.all()
        sol_header=sol_text.objects.all()
        return render(request,'solutions.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})

def partners(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=p_artners.objects.all()
        par_header=part_text.objects.all()
        return render(request,'partners.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=p_artners_french.objects.all()
        par_header=part_text_french.objects.all()
        return render(request,'fr/partners.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=p_artners.objects.all()
        par_header=part_text.objects.all()
        return render(request,'partners.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"par_header":par_header})

def dynamic_lookup_view_partners(request,name):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = p_artners.objects.get(Service_name=name)
        obj_all = p_artners.objects.filter(~Q(Service_name=name))
        obj_sub = Sub_Partners.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"blog-single.html",context)

    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        obj = p_artners_french.objects.get(Service_name=name)
        obj_all = p_artners_french.objects.filter(~Q(Service_name=name))
        obj_sub = Sub_Partners_french.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"fr/blog-single.html",context)
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = p_artners.objects.get(Service_name=name)
        obj_all = p_artners.objects.filter(~Q(Service_name=name))
        obj_sub = Sub_Partners.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"blog-single.html",context)


def dynamic_lookup_view_solutions(request,name):
    request.session['solution']=name
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = solutions.objects.get(tag=name)
        obj_all = solutions.objects.filter(~Q(tag=name))
        obj_sub = Sub_Solutions.objects.get(tag=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"blog-single.html",context)
    elif(request.session['lang']=='fr'):
        # trans=Translator.translate(name)
        # print(trans)
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        obj = solutions_french.objects.get(tag=name)
        obj_all = solutions_french.objects.filter(~Q(tag=name))
        obj_sub = Sub_Solutions_french.objects.filter(tag=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan
        }
        return render(request,"fr/blog-single.html",context)
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = solutions.objects.get(tag=name)
        obj_all = solutions.objects.filter(~Q(Service_name=name))
        obj_sub = Sub_Solutions.objects.filter(tag=name)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }

        return render(request,"blog-single.html",context)
def dynamic_lookup_view_sub_solutions(request,name,tag):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = Sub_Solutions.objects.get(Service_name=name)
        obj_all = solutions.objects.all()
        obj_sub = Sub_Solutions.objects.filter(tag=name)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"blog-single-1.html",context)
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        translate=Translator()
        brand1=brand_text_french.objects.all()

        if (Sub_Solutions_french.objects.get(Service_name_english=name)):
            obj = Sub_Solutions_french.objects.get(Service_name_english=name)
            obj_all = solutions.objects.all()
            obj_sub = Sub_Solutions.objects.filter(tag=name)
            context={
                "object":obj,
                "brand1":brand1,
                "lan":lan,
                "obj_all":obj_all,
                "obj_sub":obj_sub,
            }
        
            return render(request,"fr/blog-single-1.html",context)
        else:

            return render('solutions/'+request.session['solution'])
            # obj = Sub_Solutions_french.objects.get(Service_name=name)
            # obj_all = solutions.objects.all()
            # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
            # context={
            #     "object":obj,
            #     "brand1":brand1,
            #     "lan":lan,
            #     "obj_all":obj_all,
            #     "obj_sub":obj_sub,
            # }
        
            # return render(request,"fr/blog-single-1.html",context)
    else:
        from django.db.models import Q
        translate=Translator()
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = Sub_Solutions.objects.get(Service_name=name)
        obj_all = solutions.objects.all()
        obj_sub = Sub_Solutions.objects.filter(tag=name)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"blog-single-1.html",context)



def dynamic_lookup_view_sub_partners(request,name):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = Sub_Partners.objects.get(Service_name=name)
    # obj_all = solutions.objects.all()
    # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan
            # "obj_all":obj_all,
            # "obj_sub":obj_sub,
        }
        return render(request,"blog-single-1.html",context)
    elif(request.session['lang']=='fr'):

        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        obj = Sub_Partners_french.objects.get(Service_name=name)
    # obj_all = solutions.objects.all()
    # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan
            # "obj_all":obj_all,
            # "obj_sub":obj_sub,
        }
        return render(request,"fr/blog-single-1.html",context)
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = Sub_Partners.objects.get(Service_name=name)
    # obj_all = solutions.objects.all()
    # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan
            # "obj_all":obj_all,
            # "obj_sub":obj_sub,
        }
        return render(request,"blog-single-1.html",context)
from django.contrib import messages
def contact(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        mess=request.POST['mess']
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        # ''' End reCAPTCHA validation '''
        mail_list=['gmail.com','yahoo.com']
        email_domain=email.split('@')[1]
        valid_email=False
        for i in mail_list:
            if i == email_domain:
                valid_email=True
                break
            else:
                valid_email=False
        if (result['success'] and valid_email==True):
            data= contact_info(Name=name,Email=email,Subject=subject,Mess=mess)
            data.save()
            messages.info(request,'Your Message has been sent to CLOUD8020 ! You will be contacted soon !')
        else:
            messages.error(request, 'Could Not Submit your Message . Please Try Again')
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        # request.session['lang']=='fr'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        con_email=contactModel_Email.objects.all()
        con_phone=contactModel_Phone.objects.all()
        con_add=contactModel_Address.objects.all()
        return render(request,'contact.html',{'brand1': brand1,"con_email":con_email,"con_phone":con_phone,"con_add":con_add,"lan":lan})
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        con_email=contactModel_Email_french.objects.all()
        con_phone=contactModel_Phone_french.objects.all()
        con_add=contactModel_Address_french.objects.all()
        return render(request,'fr/contact.html',{'brand1': brand1,"con_email":con_email,"con_phone":con_phone,"con_add":con_add,"lan":lan})
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        con_email=contactModel_Email.objects.all()
        con_phone=contactModel_Phone.objects.all()
        con_add=contactModel_Address.objects.all()
        return render(request,'contact.html',{'brand1': brand1,"con_email":con_email,"con_phone":con_phone,"con_add":con_add,"lan":lan})
def update_session(request):
    res=''
    sub_url=''
    req_url=''
    sen=''
    if ( request.session['lang'] == 'fr'):

        request.session['lang'] = 'ENG'
        sub_url=request.GET['u']
        # res=sub_url.split('/',-2)
        # if res[1]=='solutions':
        #     req_url=mark_safe(res[2])
        #     req_url=req_url.replace('%20',' ')
        #     translator=Translator()
        #     sen = translator.translate(str(req_url),dest='en')
        #     return redirect('http://cloud8020.com/solutions/'+str(mark_safe(sen.text)).title()+'/')
        return redirect(sub_url)
    else:
        request.session['lang'] = 'fr'
        sub_url=request.GET['u']
        # res=sub_url.split('/',-2)
        # if res[1]=='solutions':
        #     req_url=res[2]
        #     req_url=req_url.replace('%20',' ')
        #     translator=Translator()
        #     sen = translator.translate(str(req_url),src='en',dest='fr')
        #     return redirect('http://cloud8020.com/solutions/'+str(mark_safe(sen.text)).title()+'/')
        return redirect(sub_url)
        
    # return HttpResponse('You submitted: %r' % mark_safe(sen.text))
    # sub_url=request.GET['u']
    # return redirect(request.GET['u'])


def dynamic_lookup_view_job(request,country,state,type,title):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = jobs.objects.get(Country=country)
        obj_all = jobs.objects.filter(~Q(Country=country))
        obj_sub = jobs.objects.filter(Country=country)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"job_details.html",context)
        
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        obj = jobs.objects.get(Country=country)
        obj_all = jobs.objects.filter(~Q(Country=country))
        obj_sub = jobs.objects.filter(Country=country)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
        }
        return render(request,"fr/blog-single.html",context)
    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = jobs.objects.get(Country=country)
        obj_all = jobs.objects.filter(~Q(Country=country))
        obj_sub = jobs.objects.filter(Country=country)
        context={
            "object":obj,
            "brand1":brand1,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
            "lan":lan,
            
        }
        return render(request,"job_details.html",context)

def projects(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=projects_data.objects.all()
        sol_header=project_header.objects.all()
        return render(request,'projects.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=projects_data_french.objects.all()
        sol_header=projects_data_french.objects.all()
        return render(request,'fr/projects.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})

    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=projects_data.objects.all()
        sol_header=project_header.objects.all()
        return render(request,'projects.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header})  


def corp_training(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=corpo_data.objects.all()
        sol_header=corpo_header.objects.all()
        sub_corpo_data=corpo_sub_data.objects.all()
        return render(request,'corpo.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=corpo_data_french.objects.all()
        sol_header=corpo_header_french.objects.all()
        sub_corpo_data=corpo_sub_data_french.objects.all()

        return render(request,'fr/corpo.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})

    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=corpo_data.objects.all()
        sol_header=corpo_header.objects.all()
        sub_corpo_data=corpo_sub_data.objects.all()

        return render(request,'corpo.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})    




def dynamic_lookup_view_sub_corporate_data(request,tag):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = corpo_sub_data.objects.get(Sub_tag=tag)
        obj_all = corpo_sub_data.objects.all()
        obj_sub = corpo_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"sub_corpo.html",context)
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        translate=Translator()
        brand1=brand_text_french.objects.all()

        if (corpo_sub_data_french.objects.get(Sub_tag=tag)):
            obj = corpo_sub_data_french.objects.get(Sub_tag=tag)
            obj_all = corpo_sub_data_french.objects.all()
            obj_sub = corpo_sub_data_french.objects.filter(Sub_tag=tag)
            context={
                "object":obj,
                "brand1":brand1,
                "lan":lan,
                "obj_all":obj_all,
                "obj_sub":obj_sub,
            }
        
            return render(request,"fr/sub_corpo.html",context)
        else:

            return render('solutions/'+request.session['solution'])
            # obj = Sub_Solutions_french.objects.get(Service_name=name)
            # obj_all = solutions.objects.all()
            # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
            # context={
            #     "object":obj,
            #     "brand1":brand1,
            #     "lan":lan,
            #     "obj_all":obj_all,
            #     "obj_sub":obj_sub,
            # }
        
            # return render(request,"fr/blog-single-1.html",context)
    else:
        from django.db.models import Q
        translate=Translator()
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = corpo_sub_data.objects.get(Sub_tag=tag)
        obj_all = corpo_sub_data.objects.all()
        obj_sub = corpo_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"sub_corpo.html",context)
def cctraining(request):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=career_data.objects.all()
        sol_header=career_header.objects.all()
        sub_corpo_data=career_sub_data.objects.all()
        return render(request,'career.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})
    elif (request.session['lang']=='fr'):
        lan=request.session['lang']
        brand1=brand_text_french.objects.all()
        solution_data=career_data_french.objects.all()
        sol_header=career_header_french.objects.all()
        sub_corpo_data=career_sub_data_french.objects.all()

        return render(request,'career.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})

    else:
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        solution_data=career_data.objects.all()
        sol_header=career_header.objects.all()
        sub_corpo_data=career_sub_data.objects.all()

        return render(request,'career.html',{'brand1': brand1,"solutions":solution_data,"lan":lan,"sol_header": sol_header,"sub_corp":sub_corpo_data})    


def dynamic_lookup_view_sub_careerchange_data(request,tag):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = career_sub_data.objects.get(Sub_tag=tag)
        obj_all = career_sub_data.objects.all()
        obj_sub = career_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"career_details.html",context)
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        translate=Translator()
        brand1=brand_text_french.objects.all()

        if (career_sub_data_french.objects.get(Sub_tag=tag)):
            obj = career_sub_data_french.objects.get(Sub_tag=tag)
            obj_all = career_sub_data_french.objects.all()
            obj_sub = career_sub_data_french.objects.filter(Sub_tag=tag)
            context={
                "object":obj,
                "brand1":brand1,
                "lan":lan,
                "obj_all":obj_all,
                "obj_sub":obj_sub,
            }
        
            return render(request,"career_details.html",context)
        else:

            return render('solutions/'+request.session['solution'])
            # obj = Sub_Solutions_french.objects.get(Service_name=name)
            # obj_all = solutions.objects.all()
            # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
            # context={
            #     "object":obj,
            #     "brand1":brand1,
            #     "lan":lan,
            #     "obj_all":obj_all,
            #     "obj_sub":obj_sub,
            # }
        
            # return render(request,"fr/blog-single-1.html",context)
    else:
        from django.db.models import Q
        translate=Translator()
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = career_sub_data.objects.get(Sub_tag=tag)
        obj_all = career_sub_data.objects.all()
        obj_sub = career_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"career_details.html",context)


def dynamic_lookup_view_sub_careerchange_data_register(request,tag):
    if 'lang' not in request.session:
        request.session['lang']='ENG'
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = career_sub_data.objects.get(Sub_tag=tag)
        obj_all = career_sub_data.objects.all()
        obj_sub = career_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"career_register.html",context)
    elif(request.session['lang']=='fr'):
        lan=request.session['lang']
        translate=Translator()
        brand1=brand_text_french.objects.all()

        if (career_sub_data_french.objects.get(Sub_tag=tag)):
            obj = career_sub_data_french.objects.get(Sub_tag=tag)
            obj_all = career_sub_data_french.objects.all()
            obj_sub = career_sub_data_french.objects.filter(Sub_tag=tag)
            context={
                "object":obj,
                "brand1":brand1,
                "lan":lan,
                "obj_all":obj_all,
                "obj_sub":obj_sub,
            }
        
            return render(request,"career_register.html",context)
        else:

            return render('solutions/'+request.session['solution'])
            # obj = Sub_Solutions_french.objects.get(Service_name=name)
            # obj_all = solutions.objects.all()
            # obj_sub = Sub_Solutions.objects.filter(Main_Service=name)
            # context={
            #     "object":obj,
            #     "brand1":brand1,
            #     "lan":lan,
            #     "obj_all":obj_all,
            #     "obj_sub":obj_sub,
            # }
        
            # return render(request,"fr/blog-single-1.html",context)
    else:
        from django.db.models import Q
        translate=Translator()
        lan=request.session['lang']
        brand1=brand_text.objects.all()
        obj = career_sub_data.objects.get(Sub_tag=tag)
        obj_all = career_sub_data.objects.all()
        obj_sub = career_sub_data.objects.filter(Sub_tag=tag)
        context={
            "object":obj,
            "brand1":brand1,
            "lan":lan,
            "obj_all":obj_all,
            "obj_sub":obj_sub,
        }
        return render(request,"career_register.html",context)

@csrf_exempt
def dynamic_lookup_view_sub_careerchange_data_register_success(request,tag):
    name=request.GET['name']
    email=request.GET['email']
    # return 
    description=request.GET['desc']
    mobile=request.GET['Mobile']
    amt=request.GET['amt']
    career_training_form(Name=name,Email=email,Description=description,Mobile=mobile,amt=amt).save()
    return redirect('index')

