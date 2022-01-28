from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rotate', views.rotate, name='rotate'),
    path('flip', views.flip, name='flip'),
    path('crop', views.crop, name='crop'),
    path('resolution', views.resolution, name='resolution'),
    path('contrast', views.contrast, name='contrast'),

]