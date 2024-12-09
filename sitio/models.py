from django.db import models
from django.contrib.auth.models import User
from sitio.choices import categoria, estado, valido



# Create your models here.

#Tabla de Perfiles
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fotoperfil = models.ImageField(upload_to='fotos_perfil/', verbose_name="Foto", blank=True, null=True)
    fechanac = models.DateField(verbose_name="Fecha_Nacimiento")
    verificacion = models.CharField(max_length=45, choices=valido, default='0', verbose_name="Verificacion")
    
    
    class Meta:
        db_table = 'perfil'
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"


#Tabla de Servicio
class servicio(models.Model):
    fotoprincipal = models.ImageField(upload_to='fotos_services/', verbose_name="Foto_service", blank=True, null=True)
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    cate = models.CharField(max_length=45,choices=categoria,default='0',verbose_name="Categoria")
    descripcion = models.CharField(max_length=500,verbose_name="Descripcion")
    costo = models.CharField(max_length=10,verbose_name="Precio")
    limite = models.PositiveIntegerField(default=5,verbose_name="Limites")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'servicio'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

class estate(models.Model):
    state = models.CharField(max_length=100,choices=estado,default='0',verbose_name="Estado")
    id_servicio = models.ForeignKey(servicio,null=False,on_delete=models.RESTRICT)
    id_user = models.ForeignKey(User,null=False,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'estado'
        verbose_name = "Estado"
        verbose_name_plural = "Estados"


class comentario(models.Model):
    id_perfil = models.ForeignKey(Perfil,null=False,on_delete=models.RESTRICT)
    id_servicio = models.ForeignKey(servicio,null=False,on_delete=models.RESTRICT)
    comentario = models.CharField(max_length=500,verbose_name="Comentario")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')


    class Meta:
        db_table = 'comentario'
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

class calificacion(models.Model):
    nota = models.PositiveIntegerField(verbose_name="Porcentaje")
    id_perfil = models.ForeignKey(Perfil,null=False,on_delete=models.RESTRICT)
    id_servicio = models.ForeignKey(servicio,null=False,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'calificacion'
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"
        unique_together = ('id_perfil', 'id_servicio')

class calendario(models.Model):
    entrada = models.TimeField()
    salida = models.TimeField()

    class Meta:
        db_table = 'calendario'
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"

class horario(models.Model):
    fecha = models.DateField()
    id_perfil = models.ForeignKey(Perfil,null=False,on_delete=models.RESTRICT)
    id_calendario = models.ForeignKey(calendario,null=False,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'horario'
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

class imagenes(models.Model):
    foto = models.CharField(max_length=200,verbose_name="Foto")
    id_servicio = models.ForeignKey(servicio,null=False,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'imagenes'
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"


class Ticket(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    servicio = models.ForeignKey(servicio, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets")
    descripcion = models.TextField(verbose_name="Descripción")
    estado = models.CharField(max_length=20, choices=estado, default='0', verbose_name="Estado")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f"Ticket #{self.id} - {self.usuario.username} ({self.get_estado_display()})"

    class Meta:
        db_table = "ticket"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

