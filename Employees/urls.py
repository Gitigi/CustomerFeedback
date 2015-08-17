from django.conf.urls import url

urlpatterns = [
    url(r'^$','Employees.views.Employee_page',name = 'employee'),
    url(r'^login$','Employees.views.Employee_login',name='login'),
    url(r'^logout$','Employees.views.Employee_logout',name='logout'),
    url(r'^company_feedback/(.+)/','Employees.views.Company_feedback',name='company_feedback')
    ]
