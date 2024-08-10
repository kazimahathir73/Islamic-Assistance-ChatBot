from django.urls import path
from . import views

urlpatterns = [
    path('',views.function, name = 'function'),
    path('getResponse', views.getResponse, name='getResponse')
]
