from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
# class Test(APIView):
#     def get(self, request):
#         return Response({'msg':'prueba'},status=status.HTTP_200_OK)

# Custom permisson for auth only users with group CAJERO
class IsCajero(BasePermission):
    def has_permission(self,request,view):
        group = request.headers.get('X-Group')
        
        if not group:
            return False
        
        if group != 'CAJERO':
            return False
        
        return True

# Custom class permission for auth only users with group CONTADOR
class IsContador(BasePermission):
    def has_permission(self,request,view):
        group = request.headers.get('X-Group')
        
        if not group:
            return False
        
        if group != 'CONTADOR':
            return False
        
        return True


class LoginService:
    @staticmethod
    def auth_user(username,password):
        #Get User
        user = get_object_or_404(User,username=username)
        
        # Validate password
        if not user.check_password(password):
            raise AuthenticationFailed("Credenciales invalidas")
        return user
    

    @staticmethod
    def login_user(username,password):
        user = LoginService.auth_user(username,password)
        token,_ = Token.objects.get_or_create(user=user)
        group = user.groups.first()
        return {"token":token.key,"group":group.name}
                
        
#Login users
@api_view(['POST'])
def login(request):
    try:
        # Load data
        username = request.data["username"]
        password = request.data["password"]
        
        # Use LoginService
        result = LoginService.login_user(username,password)
        
        return Response(result, status=status.HTTP_200_OK)
    except AuthenticationFailed as e:
        return Response({"error":e.detail}, status=status.HTTP_401_UNAUTHORIZED)
        
