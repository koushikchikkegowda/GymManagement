from django.shortcuts import render,redirect,reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from customer.models import sales


@login_required
def saleAdd(request):
    return render(request, 'sales/addSale.html')

@login_required
def addSalesItems(request):
    if request.method == "POST":
        salesObject = sales()
        salesObject.customerName=request.POST["customer"]
        
        salesObject.startDate=datetime.strptime(request.POST["start_date"], "%m/%d/%Y")
        salesObject.endDate=datetime.strptime(request.POST["end_date"], "%m/%d/%Y")
        salesObject.phone=request.POST["phone"]
        salesObject.NewOrOld=request.POST["NewOrOld"]
        salesObject.PtOrNor=request.POST["PtOrNor"]
        salesObject.Employee=request.POST["employee"]
        salesObject.price=request.POST["price"]
        salesObject.save()

        return redirect(reverse('customerList'))

@login_required
def saleList(request):
    
    all_sales = sales.objects.all()
    context={
        "sales":all_sales
    }
    return render(request,'sales/saleList.html',context)