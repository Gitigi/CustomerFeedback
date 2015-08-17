from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from Employees.models import Employee
from Companies.models import Company
from django.contrib.auth import get_user_model
User = get_user_model()

def Employee_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        arg={'firstname':request.POST.get('firstname','none'),
             'lastname':request.POST.get('lastname','none'),
             'passwd':request.POST.get('passwd','none')}
        
        username = arg['firstname']+arg['lastname']
        password = arg['passwd']
        employee = authenticate(username=username,password=password)
        if employee:
            login(request,employee)
            return redirect('employee')
        else:
            return redirect('home_page')

def Employee_logout(request):
    logout(request)
    return redirect('home_page')

def Employee_page(request):
    lastname = request.user.last_name
    employe = Employee.objects.get(lastname = lastname)
    return render(request,'employe.html',{'employe':employe})

def Company_feedback(request,company_name):
    company = Company.objects.get(name= company_name)
    employee = company.employe
    user = User.objects.get(last_name = employee.lastname)

    #check if user is logged in
    if user != request.user:
        return redirect('home_page')
        
    return render(request,'company_feedback.html',{'company':company})
