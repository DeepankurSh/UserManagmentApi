from django.urls import path
from . import views
from .views import *


urlpatterns = [

    path('',ListusersAPIView.as_view(),name = 'users'),
    path('create',CreateusersAPIView.as_view(), name ='create'),
    path('update/<str:pk>/',UpdateusersAPIView.as_view(), name = 'update'),
    path('delete/<str:pk>/',DeleteusersAPIView.as_view(), name = 'delete'),
]