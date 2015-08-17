from django.conf.urls import url

urlpatterns = [
    url(r'^feedback/(.+)/$','Customer.views.feedback_page',name='feedback')
        ]
    
