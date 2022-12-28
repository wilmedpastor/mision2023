from django.urls import path,include
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='inicio'),
    path('eventos', views.eventos, name='eventos'),    
    path('contacto', views.contacto, name='contacto'),    
    path('pastores', views.pastores, name='pastores'),    
    path('ministerios', views.ministerios, name='ministerios'),    
    path('doctrina', views.doctrina, name='doctrina'),    
    path('misionvision', views.misionvision, name='misionvision'),    
    path('servicios', views.servicios, name='servicios'),    
    path('videoanuncios', views.videoanuncios, name='videoanuncios'),    
    path('desclibros', views.desclibros, name='desclibros'),    
    path('privado/', include('aplicaciones.privado.urls')),    
     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)