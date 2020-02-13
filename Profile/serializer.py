from rest_framework import routers , serializers, viewsets

#----agregando modelos

from Profile.models import Profile,Ciudad,Genero,Ocupacion,Estado,Estadocivil

class ProfileSerializers (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class CiudadSerializers (serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class GeneroSerializers (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')

class OcupacionSerializers (serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('__all__')

class EstadoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')

class EstadocivilSerializers (serializers.ModelSerializer):
    class Meta:
        model = Estadocivil
        fields = ('__all__')