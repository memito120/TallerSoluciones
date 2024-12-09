from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
#Modelos
from django.contrib.auth.models import User
from sitio.models import Perfil,servicio, comentario, calificacion, estate, Ticket
from sitio.choices import categoria, OPCIONES_SERVICIO


class CustomUserCreationForm(UserCreationForm):
    pass

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user

# Formulario para el Perfil
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['fotoperfil', 'fechanac']

#Formulario para el Servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = ['fotoprincipal','nombre', 'cate', 'descripcion', 'costo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si quieres predefinir el valor de la categoría en el formulario
        self.fields['cate'].initial = '1'

#Formulario para el Estado
class EstadoForm(forms.ModelForm):
    class Meta:
        model = estate
        fields = ['state']  # Solo permitimos modificar el estado


#Formularios para comentarios
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = comentario
        fields = ['comentario']

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = comentario
        fields = ['comentario']

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = calificacion
        fields = ['nota']


class TicketForm(forms.ModelForm):

    servicio_tipo = forms.ChoiceField(
        choices=OPCIONES_SERVICIO,
        widget=forms.RadioSelect,
        required=True,
        label="Seleccione el tipo de servicio",
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label="Descripción del problema",
    )

    class Meta:
        model = Ticket
        fields = ['servicio', 'descripcion']

    def __init__(self, *args, **kwargs):
        servicios_creados = kwargs.pop('servicios_creados', servicio.objects.none())
        servicios_comprados = kwargs.pop('servicios_comprados', servicio.objects.none())
        super().__init__(*args, **kwargs)

        # Convertir a querysets si no lo son
        if isinstance(servicios_creados, list):
            servicios_creados = servicio.objects.filter(id__in=[s.id for s in servicios_creados])
        if isinstance(servicios_comprados, list):
            servicios_comprados = servicio.objects.filter(id__in=[s.id for s in servicios_comprados])

        # Combinar querysets
        self.fields['servicio'].queryset = servicios_creados | servicios_comprados
        self.fields['servicio'].required = False  # Permitimos "Otros"

