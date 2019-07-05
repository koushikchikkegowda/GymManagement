from django.shortcuts import render,redirect,reverse
from .models import Customer
from django.contrib.auth.decorators import login_required
# from .models import Retailer,Customer,User,Role,Permissions,Category,Retailer_subscription,Retailer_payment,Subscription
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .decorators import permission_required
# from .filters import RetailerFilter
# import datetime
# from django.urls import reverse

@login_required
def customerList(request):
    
    all_customers = Customer.objects.all()
    print(all_customers)
    context={
        "customers":all_customers
    }
    print('hi')
   
    return render(request,'customer/customerList.html',context)