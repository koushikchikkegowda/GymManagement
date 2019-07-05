from django.shortcuts import render,redirect,reverse
from customer.models import Employee
from django.contrib.auth.decorators import login_required




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
    # Employee = Employee.objects.all()
    # context={
       
    #     "membership":memberships
    # }
    return render(request, 'employee/employeeAdd.html')