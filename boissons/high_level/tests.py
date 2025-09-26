from django.test import TestCase
from .models import Localisation, Local, Machine, MatierePremiere, ApprovisionnementMatierePremiere
from .models import Metier


class CostCalculationTestCase(TestCase):
    def test_local_costs(self):
        self.assertEqual(Metier.objects.count(), 0)
        Metier.objects.create(nom="Mélangeur", remuneration=10)
        self.assertEqual(Metier.objects.count(), 1)







class CoutTestCase(TestCase):
    def setUp(self):
        # Création de la localisation
        self.labege = Localisation.objects.create(
            nom="Labège",
            taxes=0,
            prix_m2=2000
        )

        # Création du local
        self.local = Local.objects.create(
            nom="Atelier",
            localisation=self.labege,
            surface=50
        )

    def test_local_costs(self):
        self.assertEqual(self.local.costs(), 100000)

 
        sucre = MatierePremiere.objects.create(
            nom="Sucre", stock=1000, emprise=0
        )
        eau = MatierePremiere.objects.create(
            nom="Eau", stock=50, emprise=0
        )

        ApprovisionnementMatierePremiere.objects.create(
            quantite=1000,
            matiere_premiere=sucre,
            localisation=self.labege,
            prix_unitaire=10,
            delais=2
        )
        ApprovisionnementMatierePremiere.objects.create(
            quantite=50,
            matiere_premiere=eau,
            localisation=self.labege,
            prix_unitaire=15,
            delais=1
        )

def test_matiere_costs(self):
        total = sum(a.costs() for a in ApprovisionnementMatierePremiere.objects.all())
        self.assertEqual(total, 10750) 
# Machines
        Machine.objects.create(
            nom="Machine1",
            prix_achat=2000,
            cout_maintenance=1000,
            operateurs=1,
            debit=10,
            surface=10,
            debit_energie=1,
            taux_utilisation=80,
            local=self.local
        )
        Machine.objects.create(
            nom="Machine2",
            prix_achat=1000,
            cout_maintenance=2000,
            operateurs=1,
            debit=20,
            surface=15,
            debit_energie=2,
            taux_utilisation=90,
            local=self.local
        )
def test_machine_costs(self):
        total = sum(m.costs() for m in self.local.machine_set.all())
        self.assertEqual(total, 1000)
