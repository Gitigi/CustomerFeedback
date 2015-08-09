from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from Employees.models import Employee

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
