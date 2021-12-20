
from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.product_list, name='view'),
    re_path('signup', views.signup, name='signup'),
    re_path('contact', views.contact, name='contact'),
    re_path('about', views.about, name='about'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    re_path('person', views.personal, name='personal'),
    re_path('updateimage', views.updateimage, name='updateimage'),
    re_path(r'order/(?P<id>\d+)',views.detail_view,name='detail_view'),
   
    re_path(r'check/(?P<id>\d+)', views.Pdf.as_view()),
    re_path('logou',views.logout,name='logout'),
    


    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
] 