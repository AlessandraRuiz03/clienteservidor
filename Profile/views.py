
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Profile.models import Profile, Ciudad,Genero,Ocupacion,Estado,Estadocivil
from Profile.serializer import ProfileSerializers, CiudadSerializers, GeneroSerializers, OcupacionSerializers, EstadoSerializers, EstadocivilSerializers


class ProfileList(APIView):
    #metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):

    def get(self, request, format=None):
        print("Metodo get filter ciudad")
        queryset = Ciudad.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):

    def get(self, request, format=None):
        print("Metodo get filter genero")
        queryset = Genero.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):

    def get(self, request, format=None):
        print("Metodo get filter ocupacion")
        queryset = Ocupacion.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter estado")
        queryset = Estado.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class EstadocivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter estadocivil")
        queryset = Estadocivil.objects.filter(delete =False)
        #many = true si aplica si retorno multiples objetos
        serializer = EstadocivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadocivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

