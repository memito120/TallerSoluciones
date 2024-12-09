from rest_framework import serializers
from sitio.models import servicio

class ServicioSerializar(serializers.ModelSerializer):
    class Meta:
        model = servicio
        fields = '__all__'  
