from django.shortcuts import render,redirect
from django.http import HttpResponse
from Customer.models import Company

def home_page(request):
    companies = Company.objects.all()
    return render(request,'home.html',{'companies':companies })

def feedback_page(request,company_name):
    return render(request,'feedback.html')
