from django.contrib import admin
from .models import membership,Customer,Employee,sales
# from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(membership)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(sales)
