from django.urls import path
from . import views

urlpatterns =[
    path('index',views.index,name='index'),
    path('base',views.base,name='base'),
    path('deportes',views.deportes,name='deportes'),
    path('nacional',views.nacional,name='nacional'),
    path('noticiaInternacional',views.noticiaInternacional,name='noticiaInternacional'),
    path('carrito',views.carrito,name='carrito'),
    path('registro',views.registro,name='registro'),
]