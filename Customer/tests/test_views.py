from django.test import TestCase
from Customer.models import Company
from unittest.mock import patch,Mock

class CustomerTest(TestCase):

    def test_home_page_renders_correct_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_home_uses_company(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['companies'],Company)

    @patch('Customer.models.Company')
    def test_user_is_presented_with_a_form_after_selecting_a_comapnay(
        self,mockCustomer):

        response = self.client.get('/feedback/google/')
        self.assertTemplateUsed(response,'feedback.html')
