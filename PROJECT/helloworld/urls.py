from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='index'),
    path('services/', views.services, name='index_1'),
    # path('gallery/', views.gallery, name='index'),
    path('solutions/',views.solution,name='solution_url'),
    path('jobs/',views.job,name='solutions'),
    path('partners/',views.partners,name='partners'),
    path('contact/',views.contact,name='solutions'),
    path('solutions/<str:name>/',views.dynamic_lookup_view_solutions,name='solutions'),
    path('corporate-training/<str:tag>/',views.dynamic_lookup_view_sub_corporate_data,name='Corporate Data'),

    path('solutions/subsolutions/<str:name>/<str:tag>/view',views.dynamic_lookup_view_sub_solutions,name='solutions'),
    path('partners/<str:name>/view',views.dynamic_lookup_view_partners,name='solutions'),
    path('partners/subpartners/<str:name>/view',views.dynamic_lookup_view_sub_partners,name='solutions'),
    path('excel/',views.update_session,name="downloadexcel"),
    path('search/',views.job_search,name="search"),
    path('jobs/<str:country>/<str:state>/<str:type>/<str:title>/',views.dynamic_lookup_view_job,name='solutions'),
    # path('projects/',views.projects,name='projects'),
    path('corporate-training/',views.corp_training,name='Corporate-Training'),
    path('career-change-training/',views.cctraining,name="cctrain"),
    path('career-change-training/<str:tag>/',views.dynamic_lookup_view_sub_careerchange_data,name='Career Data'),
    path('career-change-training/<str:tag>/register/',views.dynamic_lookup_view_sub_careerchange_data_register,name='Career Data Register'),
    path('career-change-training/<str:tag>/register/success/',views.dynamic_lookup_view_sub_careerchange_data_register_success,name='Career Data Register Success'),

    


]
