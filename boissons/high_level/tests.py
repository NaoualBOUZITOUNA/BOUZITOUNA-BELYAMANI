# Create your tests here.
from django.test import TestCase


class CostCalculationTestCase(TestCase):
    def test_local_costs(self):
        self.assertEqual(Metier.objects.count(), 0)
        Metier.objects.create(nom="Mélangeur", remuneration=10)
        self.assertEqual(Metier.objects.count(), 1)
