from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from auth.views import IsContador
from pago_predial.models import Adeudo,DescuentoAdeudo
from user.models import UserNotes,Predio
from pago_predial import serializer as s


# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def load_dashboard(request):
    # #
   debt = Adeudo.objects.all().filter(estatus = 'PAGADO').order_by('-id')[:5]
   user_notes = UserNotes.objects.filter(user = request.user)
   discount_dash = DescuentoAdeudo.order_by('-fecha')[:5]
   return Response({debt,user_notes,discount_dash},status=status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def load_notifications_dashboard(request):
    return Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def load_discount_requests_dashboard(request):
    discount_dash = DescuentoAdeudo.objects.all()
    return Response({discount_dash},status=status.HTTP_200_OK)

class DiscountsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated,IsContador]
    
    # LoadDiscountRequest
    def get(self,request,*args, **kwargs):
        try:
            predio = Predio.objects.get(clave_catastral = request.data["clave_catastral"])
            data = Adeudo.objects.filter(predio = predio, ejercicio = request.data["ejercicio"])
            return Response({data},status=status.HTTP_200_OK)
        except predio.DoesNotExist:
            raise NotFound("Error al consultar los datos del predio") 

    def post(self,request,*args, **kwargs):
        serializer = s.DescuentoAdeudoSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'Descuento Aprobado'},status=status.HTTP_200_OK)

        return Response({'Error al aprobar descuento'},status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def load_discount_request(request):
    try:
        predio = Predio.objects.get(clave_catastral = request.data["clave_catastral"])
        data = Adeudo.objects.filter(predio = predio, ejercicio = request.data["ejercicio"])
        return Response({data},status=status.HTTP_200_OK)
    except predio.DoesNotExist:
        return Response({'Error al cargar datos'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def approve_discount(request):
    
    return Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsContador])
def make_report(request):
    return Response

