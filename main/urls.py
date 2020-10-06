from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.clears),
    path('count_by_2', views.addtwo),
]