from django.urls import path,include
from . import views


urlpatterns = [
    path('employeeList/',views.employeeList,name="employeeList"),
    path('employee_delete/<int:pk>',views.employee_delete, name="employee_delete"),
    # path('customer_edit/<int:pk>',views.customer_edit, name="customer_edit"),
    # path('customer_editItem/<int:pk>',views.customer_editItem, name="customer_editItem"),
    path('addEmployee/',views.addEmployee, name="addEmployee"),
    


]