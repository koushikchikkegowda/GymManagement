from django.urls import path,include
from . import views


urlpatterns = [
    path('customerList/',views.customerList,name="customerList"),
    path('customer_delete/<int:pk>',views.customer_delete, name="customer_delete"),
    path('customer_edit/<int:pk>',views.customer_edit, name="customer_edit"),
    path('customer_editItem/<int:pk>',views.customer_editItem, name="customer_editItem"),
    path('addCustomer/',views.addCustomer, name="addCustomer"),
    


]