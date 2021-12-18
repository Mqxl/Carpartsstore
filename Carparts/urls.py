
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from parts.views import SearchResultsView

 
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^', include(('parts.urls','parts'), namespace='carparts')),
    url(r'^cart/', include(('cart.urls','cart'),namespace='cart')),
    url(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
