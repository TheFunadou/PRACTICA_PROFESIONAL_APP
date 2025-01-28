from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth.models import User
from django.db import transaction
# Importar exception para manejar errores de validacion de datos
from rest_framework.exceptions import ValidationError,NotFound
from auth.views import IsContador
from decouple import config

# Create your views here.

# Save in a dictionary the id of the group loading the id from .env
GROUPS = {
    "CONTADOR":config('CONTADOR_ID'),
    "CAJERO":config('CAJERO_ID')
}


class UserSesionService():
    def __init__(self,username,token,group):
        self._username=username
            
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        self._username = username
     
    def get_user (self):
        return User.objects.get(username = self._username)
    

# The class contains the logic of register
class UserRegisterService:
    @staticmethod
    def register_user(data):
        group_name = data.get("group")
        # Check if the group exists in GROUPS
        if not (group_name in GROUPS):
            raise ValidationError("Grupo No Existente")
        
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
                user= User.objects.get(username=serializer.data.get("username"))
                # Set the password
                user.set_password(serializer.data.get("password"))
                user.groups.add(GROUPS[group_name])
                Token.objects.create(user=user)
     
            return {"Usuario Creado."}
        
# Logic of restore password request
class RestorePasswordRequestService:
    @staticmethod
    def user_exists(username):
        try:
            user = User.objects.get(username=username)
            return user
        except:
            raise NotFound('El usuario no existe')
    
    @staticmethod
    def request(username):
        user = RestorePasswordRequestService.user_exists(username)
        msg = f'El usuario {user.username} solicito una restauracion de contraseña.'
        ## ADD LOGIC FOR SEND THE NOTIFICATION TO CONTADOR FOR RESTORE PASSWORD OF USER´S
        return {'Peticion de restablecimiento de contraseña enviada con exito.'}
    
    
class RestorePasswordService:
    @staticmethod
    def set_password(username, new_password):
        try:
            # Get user
            user = User.objects.get(username = username)
            
            # set new password
            user.set_password(new_password)
            user.save
            return {f'Contraseña del usuario {user.username} cambiada satisfactoriamente.'}
        except:
            raise NotFound('Error al cambiar la contraseña, el usuario no existe')
       

# Endpoint for CREATE users
@api_view(['POST'])
def register(request):
    try:
        result = UserRegisterService.register_user(request.data)
        return Response(result, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(e.detail,status=status.HTTP_400_BAD_REQUEST)
    
# Endpoint for DELETE Users
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def delete_user(request):
    try:
        with transaction.atomic():
            user = User.objects.get(username = request.data["username"])
            user.delete()
            return Response({'msg': f'Usuario {user.username} eliminado satisfactoriamente.'},status=status.HTTP_200_OK)
    except:
        return Response({'error':'Error al eliminar al usuario'}, status=status.HTTP_400_BAD_REQUEST)

# Enpoint for send request for restore passwords
@api_view(['POST'])
def restore_password_request(request):
    restore_request = RestorePasswordRequestService(request.data["username"])
    return Response (restore_request,status=status.HTTP_200_OK)

# Endpoint for restore passwords
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def restore_password(request):
    username = request.data["username"]
    new_password = request.data["new_password"]
    restore_password = RestorePasswordService.set_password(username,new_password)
    return Response(restore_password,status=status.HTTP_200_OK)
