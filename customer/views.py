from django.shortcuts import render,redirect,reverse
from .models import Customer,membership
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
    memberships = membership.objects.all()
    context={
       
        "membership":memberships
    }
    return render(request, 'customer/addCustomer.html',context)

# @login_required
# def customer_addItem(request):
#     if request.method == "POST":
#         customer = Customer()
#         customer.username=request.POST["username"]
#         customer.email=request.POST["email"]
#         customer.password=request.POST["password"]
#         customer.fullname=request.POST["fullname"]
#         customer.mobile_number=request.POST["mobile_number"]
#         customer.gender=request.POST["gender"]
#         customer.date_of_birth=datetime.strptime(request.POST["date_of_birth"], "%m/%d/%Y")
#         customer.address=request.POST["address"]
#         customer.save()

#         return redirect(reverse('home:listCustomer'))

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
# @login_required
# def customer_editItem(request,pk):
#     if request.method == "POST":
#         print("update")
#         custObj=Customer()
#         custObj.username=request.POST["name"]
#         custObj.status=request.POST["status"]
       
#         custObj.membership_id=request.POST["membership"]
#         custObj.address=request.POST["address"]
#         custObj.phone=request.POST["phone"]
#         custObj.save()

#         return redirect(reverse('customerList'))
#     return redirect(reverse('customerList'))