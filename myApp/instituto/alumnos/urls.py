from django.urls import path # type: ignore
from . import views

urlpatterns =[
    path('index',views.index,name='index'),
    path('base',views.base,name='base'),
    path('deportes',views.deportes,name='deportes'),
    path('nacional',views.nacional,name='nacional'),
    path('noticiaInternacional',views.noticiaInternacional,name='noticiaInternacional'),
    path('carrito',views.carrito,name='carrito'),
    path('registro',views.registro,name='registro'),
    path('listaSQL',views.listaSQL,name='listaSQL'),
    path('usuarios_add',views.usuarios_add,name='usuarios_add'),
    path('usuarios_del/<str:pk>', views.usuarios_del, name='usuarios_del'),
    path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),
    path('usuarios_edit',views.usuarios_edit,name='usuarios_edit'),
    path('usuarios_list',views.usuarios_list,name='usuarios_list'),
    path('usuarioAdd',views.usuarioAdd,name='usuarioAdd'),
    path('adminUsuarioAdd',views.adminUsuarioAdd,name='adminUsuarioAdd'),
    path('crud',views.crud,name='crud'),
    path('usuariosUpdate',views.usuariosUpdate,name='usuariosUpdate'),
    path('perfil/', views.perfil, name='perfil'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('agregar-noticia/', views.agregar_noticia, name='agregar_noticia'),
    
    
]