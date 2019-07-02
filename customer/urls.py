from django.urls import path,include
from . import views


urlpatterns = [
    path('customerList/',views.customerList,name="customerList"),



]