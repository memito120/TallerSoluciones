from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, Avg
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#Formularios
from sitio.forms import UserCreationForm, PerfilForm, ServicioForm, EstadoForm, ComentarioForm, RespuestaForm, CalificacionForm, TicketForm
from django.contrib.auth import authenticate, login, logout
#Modelos
from sitio.models import servicio,Perfil, comentario, calificacion,estate, Ticket
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
''''''
def inicio(request):
    return render (request,'sitio/inicio.html')

def custom_logout(request):
    logout(request)
    # Redirige a la vista de inicio u otra URL
    return redirect('inicio')

'''

solicitudes_temporales = []
id_contador = 1

def enviar_verificacion(request):
    global solicitudes_temporales, id_contador

    if request.method == 'POST':
        texto_solicitud = request.POST.get('texto_solicitud')
        solicitud = {
            'id': id_contador,
            'usuario': request.user.username,
            'mensaje': texto_solicitud
        }
        solicitudes_temporales.append(solicitud)
        id_contador += 1  # Incrementa el contador para el próximo ID
        return redirect('inicio')

    return render(request, 'sitio/enviar_verificacion.html')

def administrar_verificaciones(request):
    global solicitudes_temporales

    if request.method == 'POST':
        # Obtén el ID de la solicitud seleccionada
        solicitud_id = int(request.POST.get('solicitud_id'))
        accion = request.POST.get('accion')  # 'aprobar' o 'rechazar'

        # Busca la solicitud correspondiente
        solicitud = next((s for s in solicitudes_temporales if s['id'] == solicitud_id), None)
        if solicitud:
            try:
                # Obtén el perfil del usuario asociado a la solicitud mediante la FK de User
                user = User.objects.get(username=solicitud['usuario'])
                Perfil = Perfil.objects.get(id_user=user)  # Accede al perfil a través de la relación inversa OneToOneField
                
                if accion == 'aprobar':
                    Perfil.verificacion = '1'  # Cambia la verificación a 1 (aprobado)
                    messages.success(request, f"El perfil de {Perfil.id_user} ha sido aprobado.")
                elif accion == 'rechazar':
                    Perfil.verificacion = '0'  # Cambia la verificación a 0 (rechazado)
                    messages.info(request, f"El perfil de {Perfil.id_user} ha sido rechazado.")

                Perfil.save()  # Guarda los cambios en la base de datos
            except User.DoesNotExist:
                messages.error(request, f"No se encontró un usuario con el nombre {solicitud['usuario']}.")
            except perfil.DoesNotExist:
                messages.error(request, f"No se encontró un perfil para el usuario {solicitud['usuario']}.")

            # Elimina la solicitud procesada de la lista temporal
            solicitudes_temporales = [s for s in solicitudes_temporales if s['id'] != solicitud_id]

    context = {'solicitudes': solicitudes_temporales}
    return render(request, 'sitio/administrar_verificaciones.html', context)

def busqueda_servicio(request):
    busqueda = request.POST.get("buscar", "")  #Término de búsqueda
    categorias_seleccionadas = request.POST.getlist("categorias")  #Categorías seleccionadas
    servi = servicio.objects.all()  #Consulta inicial

    #Filtro solo si hay categorías seleccionadas o texto de búsqueda
    if busqueda or categorias_seleccionadas:
        #Filtra por categorías si están seleccionadas
        query = Q()
        if categorias_seleccionadas:
            query &= Q(cate__in=categorias_seleccionadas)
        #filtro de búsqueda por nombre
        if busqueda:
            query &= Q(nombre__icontains=busqueda)

        # Aplica la consulta
        servi = servicio.objects.filter(query).distinct()

    #Obtiene todas las categorías
    todas_categorias = dict(servicio._meta.get_field('cate').choices)

    #Agrega el nombre legible de la categoría a cada servicio
    for s in servi:
        s.categoria_legible = todas_categorias.get(s.cate, s.cate)

    data = {
        'servicio': servi,  #Resultados filtrados
        'categorias': todas_categorias,  #Todas las categorías
        'categorias_seleccionadas': categorias_seleccionadas,  #Categorías seleccionadas
        'busqueda': busqueda,  #Término de búsqueda ingresado
    }
    return render(request, 'sitio/servicio.html', data)

def detalle_servicio(request, servicio_id):
    # Obtener el servicio específico
    servicio_obj = get_object_or_404(servicio, id=servicio_id)
    
    # Obtener el perfil del usuario actual
    perfil_usuario = Perfil.objects.get(id_user=request.user)
    
    # Verificar si el usuario ya ha dejado una calificación para este servicio
    calificacion_existente = calificacion.objects.filter(id_perfil=perfil_usuario, id_servicio=servicio_obj).first()

    # Crear los formularios de calificación y comentario
    form_calificacion = CalificacionForm()
    form_comentario = ComentarioForm()

    if request.method == 'POST':
        if 'calificacion' in request.POST:
            form_calificacion = CalificacionForm(request.POST)
            if form_calificacion.is_valid() and not calificacion_existente:
                # Guardar la calificación
                calificacion_obj = form_calificacion.save(commit=False)
                calificacion_obj.id_perfil = perfil_usuario
                calificacion_obj.id_servicio = servicio_obj
                calificacion_obj.save()
                return redirect('detalle_servicio', servicio_id=servicio_id)  # Redirigir para evitar reenvíos del formulario
        elif 'comentario' in request.POST:
            form_comentario = ComentarioForm(request.POST)
            if form_comentario.is_valid():
                # Guardar el comentario
                comentario_obj = form_comentario.save(commit=False)
                comentario_obj.id_perfil = perfil_usuario
                comentario_obj.id_servicio = servicio_obj
                comentario_obj.save()
                return redirect('detalle_servicio', servicio_id=servicio_id)

    # Obtener los comentarios y respuestas
    comentarios = comentario.objects.filter(id_servicio=servicio_obj).prefetch_related('respuestas')

    return render(request, 'sitio/detalle_servicio.html', {
        'servicio': servicio_obj,
        'calificacion_existente': calificacion_existente,
        'form_comentario': form_comentario,
        'form_calificacion': form_calificacion,
        'comentarios': comentarios,
    })

def carga_perfil(request):
    user = get_object_or_404(User, username = request.user)
    Perfil = get_object_or_404(perfil, id_user=user)

    

    data = {
        'user': user,
        'Perfil': Perfil

    }
    return render(request,'sitio/perfil.html', data)
'''

#Creacion de Usuario (Django) y Perfil
class CrearUsuarioYPerfil(View):
    def get(self, request):
        user_form = UserCreationForm()
        perfil_form = PerfilForm()
        return render(request, 'registration/creacion_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form})

    def post(self, request):
        user_form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES)

        if user_form.is_valid() and perfil_form.is_valid():
            # Guardar el User
            user = user_form.save()

            # Crear y guardar el Perfil asociado
            perfil = perfil_form.save(commit=False)
            perfil.user = user  # Asociamos el perfil al user
            perfil.save()

            return redirect('inicio')  # Redirigir después de la creación

        return render(request, 'registration/creacion_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form})

#Cargamos los Datos del Usuario Logeado
@login_required
def ver_perfil(request):
    # Obtenemos el perfil del usuario logueado
    perfil = Perfil.objects.get(user=request.user)
    
    # Renderizamos la plantilla con los datos del usuario y su perfil
    return render(request, 'sitio/perfil/perfil.html', {'perfil': perfil})

#Creacion de Servicios
@login_required  
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el servicio con el usuario logueado
            servicio = form.save(commit=False)
            servicio.user = request.user  # Asociamos el servicio al usuario logueado
            servicio.save()
            return redirect('servicio_list')  # Redirige a la lista de servicios u otra vista
    else:
        form = ServicioForm()
    
    return render(request, 'sitio/servicios/CREATE_servicio.html', {'form': form})

#Vista Personal de Servicios
@login_required
def listar_servicios(request):
    servicios = servicio.objects.filter(user=request.user)  # Solo los servicios del usuario logueado
    return render(request, 'sitio/servicios/mis_servicios.html', {'servicios': servicios})

#Editar Servicio
@login_required
def editar_servicio(request, servicio_id):
    # Cambiar 'Servicio' a 'servicio' para evitar conflictos con el nombre del modelo
    servicio_instance = get_object_or_404(servicio, id=servicio_id, user=request.user)

    # Si el formulario es enviado, procesamos los datos
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio_instance)
        if form.is_valid():
            form.save()
            return redirect('servicio_list')  # Redirigir a la lista de servicios
    else:
        # Si no es POST, mostramos el formulario con los datos actuales del servicio
        form = ServicioForm(instance=servicio_instance)

    return render(request, 'sitio/servicios/EDIT_servicio.html', {'form': form, 'servicio': servicio_instance})

#Eliminar un Servicio
@login_required
def eliminar_servicio(request, servicio_id):
    Servicio = get_object_or_404(servicio, id=servicio_id, user=request.user)

    if request.method == 'POST':  # Confirmación de eliminación
        Servicio.delete()
        return redirect('servicio_list')  # Redirigir a la lista de servicios
    
    return render(request, 'sitio/servicios/DELETE_servicio.html', {'servicio': Servicio})

#Vista de Servicios para Todos
def ver_todos_los_servicios(request):
    # Obtenemos todos los servicios inicialmente
    servicios = servicio.objects.all()

    # Filtrado por palabra clave (si la hay en la solicitud)
    palabra_clave = request.GET.get('buscar', '')  # Obtener el parámetro de búsqueda
    if palabra_clave:
        servicios = servicios.filter(nombre__icontains=palabra_clave)  # Filtra por nombre

    # Filtrado por categorías (si hay categorías seleccionadas)
    categorias_seleccionadas = request.GET.getlist('categoria')  # Obtener las categorías seleccionadas como una lista
    if categorias_seleccionadas:
        servicios = servicios.filter(cate__in=categorias_seleccionadas)  # Filtra por las categorías seleccionadas

    # Obtener todas las categorías disponibles para mostrarlas en el formulario de checkboxes
    categorias = servicio._meta.get_field('cate').choices

    return render(request, 'sitio/servicios/ver_servicios.html', {
        'servicios': servicios,
        'categorias': categorias,
        'palabra_clave': palabra_clave,
        'categorias_seleccionadas': categorias_seleccionadas,
    })

#Compra de Servicio
@login_required
def comprar_servicio(request, servicio_id):
    # Obtener el servicio que se va a comprar
    servicio_obj = get_object_or_404(servicio, id=servicio_id)

    #Verifica que el Dueño del servicio no compre su propio servicio
    if servicio_obj.user == request.user:
        messages.error(request, "No puedes comprar tu propio servicio.")
        return redirect('servicio_list_all')
    
    #Crear un nuevo registro en el modelo estate con el estado '0'
    nuevo_estado = estate.objects.create(
        id_servicio=servicio_obj,
        id_user=request.user,
        state='0'  # El estado inicial puede ser '0'
    )

    messages.success(request, f"Has comprado el servicio: {servicio_obj.nombre}")
    return redirect('servicio_list_all')  # Redirige a la lista de servicios u otra vista

#Modificar el Estado de un Servicio
@login_required
def modificar_estado_servicio(request, estate_id):
    # Obtener el estado del servicio
    estado_obj = get_object_or_404(estate, id=estate_id)

    # Verificar si el usuario es el propietario del servicio
    if estado_obj.id_servicio.user != request.user:
        messages.error(request, "No tienes permisos para modificar el estado de este servicio.")
        return redirect('servicio_list')

    # Si el formulario se envía, procesamos el cambio de estado
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado actualizado exitosamente.")
            return redirect('servicio_list')
    else:
        form = EstadoForm(instance=estado_obj)

    return render(request, 'sitio/servicios/EDIT_estado_servicio.html', {'form': form, 'estado': estado_obj})

#Visualizar los Servicios Comprados
@login_required
def servicios_comprados(request):
    # Obtener los registros de los servicios comprados por el usuario logueado
    servicios_comprados = estate.objects.filter(id_user=request.user)

    print(servicios_comprados)
    return render(request, 'sitio/perfil/ver_servicios_comprados.html', {'servicios_comprados': servicios_comprados})

#Visualizar los Servicios Vendidos
@login_required
def servicios_vendidos(request):
    # Filtrar los servicios vendidos por el usuario logueado
    servicios_vendidos = estate.objects.filter(id_servicio__user=request.user)

    return render(request, 'sitio/perfil/ver_servicios_vendidos.html', {'servicios_vendidos': servicios_vendidos})

#Visualizar Servicio Especifico
def ver_servicio(request, servicio_id):
    # Obtener el servicio por su ID
    servicio_instance = get_object_or_404(servicio, id=servicio_id)
    
    # Renderizar el template con los datos del servicio
    return render(request, 'sitio/servicios/servicio.html', {'servicio': servicio_instance})


@login_required
def servicio_detalle(request, servicio_id):
    # Obtener el servicio
    servicio_obj = get_object_or_404(servicio, id=servicio_id)
    # Obtener comentarios principales (sin padres) relacionados con este servicio
    comentarios = comentario.objects.filter(id_servicio=servicio_obj, parent__isnull=True).select_related('id_perfil')
    # Calcular promedio de calificaciones
    promedio_calificacion = calificacion.objects.filter(id_servicio=servicio_obj).aggregate(Avg('nota'))['nota__avg']

    # Formularios iniciales
    comentario_form = ComentarioForm()
    calificacion_form = CalificacionForm()
    respuesta_form = RespuestaForm()

    if request.method == 'POST':
        if 'comentario' in request.POST:
            # Guardar un comentario
            comentario_form = ComentarioForm(request.POST)
            if comentario_form.is_valid():
                nuevo_comentario = comentario_form.save(commit=False)
                nuevo_comentario.id_perfil = request.user.perfil
                nuevo_comentario.id_servicio = servicio_obj
                nuevo_comentario.save()
                return redirect('ver_servicio', servicio_id=servicio_id)

        elif 'nota' in request.POST:
            # Guardar una calificación
            calificacion_form = CalificacionForm(request.POST)
            if calificacion_form.is_valid():
                calificacion_obj, created = calificacion.objects.update_or_create(
                    id_perfil=request.user.perfil,
                    id_servicio=servicio_obj,
                    defaults={'nota': calificacion_form.cleaned_data['nota']}
                )
                return redirect('ver_servicio', servicio_id=servicio_id)

        elif 'respuesta' in request.POST:
            # Guardar una respuesta a un comentario
            respuesta_form = RespuestaForm(request.POST)
            parent_comentario_id = request.POST.get('parent_comentario_id')
            parent_comentario = get_object_or_404(comentario, id=parent_comentario_id)
            if respuesta_form.is_valid():
                nueva_respuesta = respuesta_form.save(commit=False)
                nueva_respuesta.id_perfil = request.user.perfil
                nueva_respuesta.id_servicio = servicio_obj
                nueva_respuesta.parent = parent_comentario
                nueva_respuesta.save()
                return redirect('ver_servicio', servicio_id=servicio_id)

    return render(request, 'sitio/servicios/servicio.html', {
        'servicio': servicio_obj,
        'comentarios': comentarios,
        'promedio_calificacion': promedio_calificacion,
        'comentario_form': comentario_form,
        'calificacion_form': calificacion_form,
        'respuesta_form': respuesta_form,
    })


#Vista para el Ticket de Soporte
class CrearTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'sitio/perfil/crear_ticket.html'
    success_url = reverse_lazy('inicio')  # Cambia esto según tu configuración

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_creados'] = servicio.objects.filter(user_id=self.request.user)
        context['servicios_comprados'] = servicio.objects.filter(
            id__in=estate.objects.filter(id_user=self.request.user).values_list('id_servicio', flat=True)
        )
        return context

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        servicios_creados = servicio.objects.filter(user=self.request.user)
        servicios_comprados = servicio.objects.filter(
            id__in=estate.objects.filter(id_user=self.request.user).values_list('id_servicio', flat=True)
        )
        print(f"Servicios creados: {servicios_creados}")
        print(f"Servicios comprados: {servicios_comprados}")
        kwargs['servicios_creados'] = servicios_creados
        kwargs['servicios_comprados'] = servicios_comprados
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario al ticket
        return super().form_valid(form)


################################

