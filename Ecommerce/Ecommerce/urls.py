from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('Cellestial.urls')),
    path('Cart/', include('Cart.urls')),
    path('admin/', admin.site.urls),
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

