from django.test import TestCase
from Customer.models import Feedback,Company

class FeedbackTest(TestCase):

    def test_feedback_save(self):
        company = Company()
        company.name = 'Google'
        company.save()
        
        feedback = Feedback()
        feedback.company = company
        feedback.firstname = 'Stephen'
        feedback.lastname = 'Gitigi'
        feedback.phone_no = '343434'
        feedback.feedback = 'what a wonderfull company'
        feedback.save()

        self.assertEqual(Company.objects.all().count(),1)
