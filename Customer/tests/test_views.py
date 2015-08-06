from django.test import TestCase
from Customer.models import Company,Feedback
from unittest.mock import patch,Mock
from django.db.models.query import QuerySet
from django.http import HttpRequest
from Customer.views import feedback_page
from unittest import skip

class CustomerUnitTest(TestCase):

    def test_home_page_renders_correct_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_home_uses_a_list_of_company(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['companies'],QuerySet)

    @patch('Customer.views.Company')
    def test_user_is_presented_with_a_form_after_selecting_a_comapnay(
        self,mockCustomer):

        response = self.client.get('/feedback/google/')
        self.assertTemplateUsed(response,'feedback.html')

    @patch('Customer.views.Company')
    @patch('Customer.views.Feedback')
    def test_redirect_after_a_POST(self,mockFeedback,mockCompany):

        data ={'first_name':'Stephen','last_name':'Gitigi','phone_no':'343434',
               'feedback':'what a wonderful company'}
        response = self.client.post('/feedback/google/',data)
        self.assertEqual(response.status_code,302)

    
    @patch('Customer.views.Company')
    @patch('Customer.views.Feedback')
    def test_feedback_saves_user_POST(self,mockFeedback,mockCompany):
        
        data ={'first_name':'Stephen','last_name':'Gitigi','phone_no':'343434',
               'feedback':'what a wonderful company'}
        request = HttpRequest()
        request.method = 'POST'
        request.POST = data

        mock_feedback = mockFeedback.return_value
        mock_company = mockCompany.objects.get.return_value
        def check_Customer_id_is_inserted_before_save():
            self.assertEqual(mock_company,mock_feedback.company)
            self.assertEqual('Stephen',mock_feedback.firstname)
            self.assertEqual('Gitigi',mock_feedback.lastname)
            self.assertEqual('343434',mock_feedback.phone_no)
            self.assertEqual('what a wonderful company',mock_feedback.feedback)

        mock_feedback.save.side_effect = check_Customer_id_is_inserted_before_save
        feedback_page(request,'Google')
        mock_feedback.save.assert_called_once_with()

class CustomerIntegratedTest(TestCase):

    def test_feedback_saves_user_POST(self):
        company = Company()
        company.name = 'Google'
        company.save()

        
        data ={'first_name':'Stephen','last_name':'Gitigi','phone_no':'343434',
               'feedback':'what a wonderful company'}
        request = HttpRequest()
        request.method = 'POST'
        request.POST = data
        feedback_page(request,'Google')
        self.assertEqual(Feedback.objects.all().count(),1)
        
