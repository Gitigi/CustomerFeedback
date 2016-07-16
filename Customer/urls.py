from django.conf.urls import url
from Customer import views as CustomerViews

urlpatterns = [
    url(r'^feedback/(.+)/$',CustomerViews.feedback_page,name='feedback')
        ]
    
