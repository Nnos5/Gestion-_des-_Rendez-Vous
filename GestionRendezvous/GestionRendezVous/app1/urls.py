from django.urls import path
from app1 import views



urlpatterns = [
 
    path('envoi/',views.envoi,name='envoi'),
    path('message/<int:pk>',views.message,name='message'),
    path('confirmation/',views.confirmation,name='confirmation')
]