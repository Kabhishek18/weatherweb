from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index),
    path('delete', views.deletecity,name='deletecity'),
  #  path('unit', views.unittestcase), #Test case
]
