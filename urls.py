from appjuntos import views
from django.urls import path
	

app_name = 'appjuntos'  


urlpatterns = [
    path('', views.index, name='index'),
    ]
