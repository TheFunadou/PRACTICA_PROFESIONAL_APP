from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from auth.views import IsCajero

# Create your views here.
# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_dashboard(request):
    return Response

# IN REVISION
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_notifications_dashboard(request):
    return Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_discount_requests_dashboard(request):
    return Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsCajero])
def load_approve_discount_data(request):
    return Response

