from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from auth.views import IsContador,IsCajero

# Endpoint for search taxpayer.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def search_taxpayer(request):
    return Response


# Endpoint for load data of taxpayer.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_taxpayer_data(request):
    return Response

# Endpoint for search taxpayer.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_taxpayer_data_with_discount(request):
    return Response


# Endpoint for search taxpayer.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def property_tax_pay(request):
    return Response

# Endpoint for search taxpayer.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def make_pay_ticket(request):
    return Response

