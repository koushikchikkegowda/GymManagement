from django.urls import path,include
from . import views


urlpatterns = [
    path('saleAdd/',views.saleAdd,name="saleAdd"),
    path('addSalesItems/',views.addSalesItems,name="addSalesItems"),
    path('saleList/',views.saleList,name="saleList"),
    


]

