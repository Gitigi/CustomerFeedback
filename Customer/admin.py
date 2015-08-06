from django.contrib import admin
from Customer.models import Company,Feedback

class CompanyAdmin(admin.ModelAdmin):
    class Meta():
        model = Company

admin.site.register(Company,CompanyAdmin)
admin.site.register(Feedback)
