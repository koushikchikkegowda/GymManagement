from django.contrib import admin
from .models import membership,Customer,Employee,sales
# Register your models here.

admin.site.register(membership)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(sales)
