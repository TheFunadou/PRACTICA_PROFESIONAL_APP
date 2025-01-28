
from user.views import register,delete_user,restore_password
from django.urls import path

urlpatterns = [
    path('register/',register),
    path('delete_user/',delete_user),
    path('restore_password/',restore_password)
]