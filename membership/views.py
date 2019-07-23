from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from customer.models import membership
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required
def membershipList(request):
    
    membership_items = membership.objects.filter(status="Active")
    context={
        "membership":membership_items
    }
    return render(request,'membership/membershipList.html',context)

@login_required
def membershipDelete(request,pk):
    membership.objects.filter(id=pk).update(status="DeActive")
    return redirect(reverse('membershipList'))


@login_required
def addMembership(request):
    return render(request, 'membership/addMembership.html')


@login_required
def addMembership_item(request):
    if request.method == "POST":
        membershipObject = membership()
        membershipObject.title=request.POST["title"]
        
        membershipObject.type=request.POST["membership"]
        membershipObject.price=request.POST["price"]
        membershipObject.duration=request.POST["duration"]
        membershipObject.status="Active"
        
        # customer.date_of_birth=datetime.strptime(request.POST["date_of_birth"], "%m/%d/%Y")
       
        membershipObject.save()

        return redirect(reverse('membershipList'))

@login_required
def membership_edit(request,pk):
    edit_membership = membership.objects.filter(status="Active",id=pk)
    context={
        "edit_membership":edit_membership
    }
    return render(request, 'membership/membershipEdit.html',context)

@login_required
def membershipEdit_item(request,pk):
     if request.method == "POST":
        title=request.POST["title"]
        type=request.POST["membership"]
        price=request.POST["price"]
        duration=request.POST["duration"]
        test=membership.objects.filter(id=pk).update(title=title,type=type,price=price,duration=duration)
        return redirect(reverse('membershipList'))
     return redirect(reverse('membershipList'))