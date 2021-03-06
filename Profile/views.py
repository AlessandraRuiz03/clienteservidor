
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework import status
from rest_framework import generics


from Profile.models import Profile, Ciudad,Genero,Ocupacion,Estado,Estadocivil
from Profile.serializer import ProfileSerializers, CiudadSerializers, GeneroSerializers, OcupacionSerializers, EstadoSerializers, EstadocivilSerializers


class ListaSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('nombre'),
                coreapi.Field('apPaterno'),
                coreapi.Field('apMaterno'),
                coreapi.Field('edad'),
                coreapi.Field('ciudad'),
                coreapi.Field('genero'),
                coreapi.Field('ocupacion'),
                coreapi.Field('estado'),
                coreapi.Field('estadocivil'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class ProfileList(APIView):
    permission_classes = []
    schema = ListaSchema()
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

class CiudadSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('ciudad'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class CiudadList(APIView):
    permission_classes = []
    schema = CiudadSchema()
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

class GeneroSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('genero'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class GeneroList(APIView):
    permission_classes = []
    schema = GeneroSchema()
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

class OcupacionSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('ocupacion'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class OcupacionList(APIView):
    permission_classes = []
    schema = OcupacionSchema()
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

class EstadoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('estado'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class EstadoList(APIView):
    permission_classes = []
    schema = EstadoSchema()
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

class EstadoCivilSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post','get'):
            extra_fields = [
                coreapi.Field('estadocivil'),
            ]
        manual_fields =super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class EstadocivilList(APIView):
    permission_classes = []
    schema = EstadoCivilSchema()
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

