from django.shortcuts import render
from sitio.models import servicio
from sitioAPI.serializers import ServicioSerializar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


@login_required
@api_view(['GET', 'POST'])
def servicio_listado(request):
    if request.method == 'GET':
        servicios = servicio.objects.all()
        serializer = ServicioSerializar(servicios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServicioSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def servicio_detalle(request, pk):
    try:
        servicio_obj = servicio.objects.get(id=pk)
    except servicio.DoesNotExist:
        return Response({'error': 'Servicio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServicioSerializar(servicio_obj)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ServicioSerializar(servicio_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        servicio_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)