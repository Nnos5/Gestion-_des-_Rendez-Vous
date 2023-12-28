from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views



urlpatterns = [
 
    path('envoi/',views.envoi,name='envoi'),
    path('confirmation/',views.confirmation,name='confirmation')
]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)