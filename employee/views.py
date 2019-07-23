from django.shortcuts import render,redirect,reverse
from customer.models import Employee
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage


@login_required
def employeeList(request):
    
    
    all_employee = Employee.objects.filter(status="Active")
    print(all_employee)
    context={
        "employee":all_employee
    }
    print('hi')
   
    return render(request,'employee/employeeList.html',context)



@login_required
def employee_delete(request,pk):
    
    Employee.objects.filter(id=pk).update(status="DeActive")
    return redirect(reverse('employeeList'))

@login_required
def addEmployee(request):
    return render(request, 'employee/employeeAdd.html')

@login_required
def addEmployee_items(request):
    if request.method == "POST":
        employee = Employee()
        #file upload
        myfile = request.FILES['identity']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        employee.IdentityProof = fs.url(filename)
        #fileuploadend
        employee.name=request.POST["name"]
        employee.joining=datetime.strptime(request.POST["joining"], "%m/%d/%Y")
        employee.designation=request.POST["designation"]
        employee.address=request.POST["address"]
        employee.phone=request.POST["phone"]
        employee.status="Active"
        
        # customer.date_of_birth=datetime.strptime(request.POST["date_of_birth"], "%m/%d/%Y")
       
        employee.save()

        return redirect(reverse('employeeList'))