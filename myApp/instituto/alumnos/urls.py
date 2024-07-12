from django.urls import path # type: ignore

from .import views

urlpatterns =[
    path('index',views.index,name='index'),
    path('base',views.base,name='base'),
    path('deportes',views.deportes,name='deportes'),
    path('nacional/', views.nacional, name='nacional'),
    path('noticiaInternacional',views.noticiaInternacional,name='noticiaInternacional'),
    path('suscripciones',views.suscripciones,name='suscripciones'),
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
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('agregar-noticia/', views.agregar_noticia, name='agregar_noticia'),
    path('validar_nombre_usuario/', views.validar_nombre_usuario, name='validar_nombre_usuario'),
    path('agregar-imagen/<int:noticia_id>/', views.agregar_imagen, name='agregar_imagen'),
    path('modificar/<int:noticia_id>/', views.modificar_noticia, name='modificar_noticia'),
    path('guardar_modificacion/<int:noticia_id>/', views.guardar_modificacion, name='guardar_modificacion'),
    path('noticia/<int:noticia_id>/', views.detalle_noticia, name='detalle_noticia'),
    path('perfil/', views.perfil, name='perfil'),
    path('eliminar-noticia/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('aprobar_noticias/', views.aprobar_noticias, name='aprobar_noticias'),
    path('cambiar_estado/<int:noticia_id>/', views.cambiar_estado_noticia, name='cambiar_estado_noticia'),
    path('checkout/', views.checkout, name='checkout'),
    path('carrito',views.carrito,name='carrito'),
    
    
    
]