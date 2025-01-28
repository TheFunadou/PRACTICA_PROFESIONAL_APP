from django.urls import path
from contador import views as v

urlpatterns = [
    path('descuentos/',v.DiscountsView.as_view())
]