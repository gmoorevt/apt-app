
from django.test import TestCase
from .models import Portfolio,Building,Unit,Lease,Tenant,Receivable,Address,Payment


# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        p = Portfolio(name='')


