
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sitio import views as vista
from sitio.views import CrearUsuarioYPerfil, CrearTicketView
from sitioAPI.views import servicio_listado, servicio_detalle  # Importar las vistas API

urlpatterns = [
    # CUENTAS
    path('admin/', admin.site.urls),
    path('', vista.inicio, name="inicio"),
    path('logout/', vista.custom_logout, name='custom_logout'),
    path('creacion/', CrearUsuarioYPerfil.as_view(), name='creacion'),
    path('accounts/', include('django.contrib.auth.urls')),

    # PERFIL
    path('perfil/', vista.ver_perfil, name='Perfil'),

    # SERVICIOS
    path('servicecreator/', vista.crear_servicio, name="creacion_servicio"),
    path('mis-servicios/', vista.listar_servicios, name='servicio_list'),
    path('todos-los-servicios/', vista.ver_todos_los_servicios, name='servicio_list_all'),
    path('servicio/editar/<int:servicio_id>/', vista.editar_servicio, name='editar_servicio'),
    path('servicio/eliminar/<int:servicio_id>/', vista.eliminar_servicio, name='eliminar_servicio'),
    path('Compra/<int:servicio_id>/', vista.comprar_servicio, name='compra_servicio'),
    path('servicios/comprados/', vista.servicios_comprados, name='servicios_comprados'),
    path('servicios/vendidos/', vista.servicios_vendidos, name='servicios_vendidos'),
    path('servicio/<int:servicio_id>/', vista.servicio_detalle, name='ver_servicio'),
    path('soporte/enviar/', CrearTicketView.as_view(), name='enviar_ticket'),

    # API REST
    path('api/servicios/', servicio_listado, name='api_servicio_listado'),
    path('api/servicios/<int:pk>/', servicio_detalle, name='api_servicio_detalle'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

