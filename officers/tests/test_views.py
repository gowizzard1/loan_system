from django.test import TestCase, Client
from unittest import TestCase
from .views import Loans

# Create your tests here.
class TestCasesLoans(unittest.TestCase):


	def test_pay_loan(self):
		
		self.assertEqual(views.pay_loan(),"here")
	
	def test_create_loan(self):
		pass


if __name__ == '__main__':
    unittest.main()