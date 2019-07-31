from django.shortcuts import render,redirect,reverse
from .models import Customer,membership
from .authentication import UserTokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
import jwt
# from .models import Retailer,Customer,User,Role,Permissions,Category,Retailer_subscription,Retailer_payment,Subscription
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .decorators import permission_required
# from .filters import RetailerFilter
# import datetime
# from django.urls import reverse

@login_required
def customerList(request):
    
    all_customers = Customer.objects.filter(status="Active")
    print(all_customers)
    context={
        "customers":all_customers
    }
    print('hi')
   
    return render(request,'customer/customerList.html',context)


@login_required
def customer_delete(request,pk):
    print("inside delete view")
    Customer.objects.filter(id=pk).update(status="DeActive")
    return redirect(reverse('customerList'))
    
@login_required
def addCustomer(request):
    print("entered")
    memberships = membership.objects.all()
    context={
       
        "membership":memberships
    }
    return render(request, 'customer/addCustomer.html',context)

@login_required
def addCustomer_items(request):
    if request.method == "POST":
        customer = Customer()
        customer.name=request.POST["name"]
        
        customer.membership_id=request.POST["membership"]
        customer.address=request.POST["address"]
        customer.phone=request.POST["phone"]
        customer.status="Active"
        
        # customer.date_of_birth=datetime.strptime(request.POST["date_of_birth"], "%m/%d/%Y")
       
        customer.save()

        return redirect(reverse('customerList'))

@login_required
def customer_edit(request,pk):
    edit_customers = Customer.objects.filter(status="Active",id=pk)
    edit_membership = membership.objects.all()
    context={
        "customers":edit_customers,
        "edit_membership":edit_membership
    }
    print(context)
    return render(request, 'customer/customerEdit.html',context)

@login_required
def customer_editItem(request,pk):
    if request.method == "POST":
        print("update")
        name=request.POST["name"]
        status=request.POST["status"]
       
        membership=int(request.POST.get("membership"))
        print(membership)
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        test=Customer.objects.filter(id=pk).update(name=name,status=status,membership_id=membership,address=address,phone=phone)
        print(test)
        return redirect(reverse('customerList'))
    return redirect(reverse('customerList'))
@api_view(["POST","GET","PUT"])
def UserLogin(request):
    print(request.data['Username'])
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")

    Username = request.data['Username']
    password = request.data['password']
    try:
        user = User.objects.get(username=Username)
        password = check_password(password=password, encoded=user.password)
        print(password)
        print(password)

    except User.DoesNotExist:
        return Response({'Error': "Invalid username/password"}, status="400")

    if user and password:
        payload = {
            'id': user.id,
            'username': user.username,
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        jwt_token = {'token': jwt.encode(payload, "SECRET").decode("utf-8")}
        print(jwt_token)

        return HttpResponse(
            json.dumps(jwt_token),
            status=200,
            content_type="application/json"
        )
    else:
        return Response(
            json.dumps({'Error': "Invalid credentials"}),
            status=400,
            content_type="application/json"
        )
# elastic search api 
@api_view(["GET"])
@authentication_classes((UserTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def ElasticCustomer(request):
    client = Elasticsearch()
    query = request.GET.get('customer')
    print(query)
    search_result = Search().using(client).query(
        "multi_match", fields=['name', 'address','phone'], query=query)
    article_result = search_result.execute().to_dict()
    print(article_result)
    return Response({
            "status":"GET",
            "Articles":article_result
        })
