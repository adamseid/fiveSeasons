from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('filter',index),
    path('home',index)
]