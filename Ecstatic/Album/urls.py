from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

app_name = 'Album'

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', views.album, name='album'),
    path('<str:title>', views.image_card, name='card'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)