from django.conf.urls import url
from Employees import views as EmployeesViews

urlpatterns = [
    url(r'^$',EmployeesViews.Employee_page,name = 'employee'),
    url(r'^login$',EmployeesViews.Employee_login,name='login'),
    url(r'^logout$',EmployeesViews.Employee_logout,name='logout'),
    url(r'^company_feedback/(.+)/',EmployeesViews.Company_feedback,name='company_feedback')
    ]
