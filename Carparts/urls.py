
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls.conf import re_path
from parts.views import SearchResultsView

 
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^', include(('parts.urls','parts'), namespace='carparts')),
    re_path(r'^cart/', include(('cart.urls','cart'),namespace='cart')),
    re_path(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
