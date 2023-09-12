from django.urls import path
from . import views

app_name ='api'
urlpatterns = [
    path('', views.stage_one_endpoint, name='stage_one_endpoint'),  
]
