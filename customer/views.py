from django.shortcuts import render,redirect,reverse
# from .models import Retailer,Customer,User,Role,Permissions,Category,Retailer_subscription,Retailer_payment,Subscription
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .decorators import permission_required
# from .filters import RetailerFilter
# import datetime
# from django.urls import reverse


def customerList(request):
    
    return render(request,'customer/customerList.html')