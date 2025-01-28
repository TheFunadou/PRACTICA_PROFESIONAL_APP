from django.contrib.auth.models import User, Group
from user import models as m
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # Campo personalizado para obtener el nombre del grupo
    group = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'group']
        extra_kwargs = {'password': {'write_only': True}}

    def get_group(self, obj):
        # Obtener el nombre del primer grupo al que pertenece el usuario
        if obj.groups.exists():
            return obj.groups.first().name
        return None  # Si el usuario no tiene grupos

    def create(self, validated_data):
        group_name = validated_data.pop('group', None)

        user = User.objects.create_user(**validated_data)

        if group_name:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

        user.save()
        return user
    
# Serializers of Contribuyente
# # NOTE (In spanish xd): Los modelos del contribuyente los decidi poner en Users para no crear una app vacia solo para poner los modelos ahi xd.

class ContribuyenteSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.Contribuyente
        fields = ['rfc','nombre','fecha_registro','correo']


class ContactoSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.Contacto
        fields = ['numero_telefonico','contribuyente','tipo']
        
class PredioSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.Predio
        fields = ['clave_catastral','contribuyente','fecha_registro','valor_catastral','num_ext','num_int','col_fracc','localidad','codigo_postal']
        

class InformacionPredioSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.InformacionPredio
        fields = ['predio','tipo','estado_fisico','superficie','uso','antiguedad','tenencia']
        
        