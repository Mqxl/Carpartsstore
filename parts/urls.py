from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='view'),
    url('signup', views.signup, name='signup'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url('person', views.personal, name='personal'),
    url('updateimage', views.updateimage, name='updateimage'),
    url(r'order/(?P<id>\d+)',views.detail_view,name='detail_view'),
   
    re_path(r'check/(?P<id>\d+)', views.Pdf.as_view()),
    url('logou',views.logout,name='logout'),
    


    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
] 