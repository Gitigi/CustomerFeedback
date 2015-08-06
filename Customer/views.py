from django.shortcuts import render,redirect
from django.http import HttpResponse
from Customer.models import Company,Feedback

def home_page(request):
    companies = Company.objects.all()
    return render(request,'home.html',{'companies':companies })

def feedback_page(request,company_name):
    if request.method == 'GET':
        company = Company.objects.get(name=company_name)
        return render(request,'feedback.html',{'company':company})
    else:
        feedback = Feedback()
        feedback.firstname = request.POST['first_name']
        feedback.lastname = request.POST['last_name']
        feedback.phone_no = request.POST['phone_no']
        feedback.feedback  = request.POST['feedback']
        
        company = Company.objects.get(name = company_name)
        feedback.company = company
        feedback.save()
        return redirect('home_page')
