from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index),
  #  path('unit', views.unittestcase), #Test case
]
