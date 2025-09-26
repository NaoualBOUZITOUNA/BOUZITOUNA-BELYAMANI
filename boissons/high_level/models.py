from django.db import models


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.IntegerField()

    def _str_(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "stock": self.stock,
            "emprise": self.emprise,
        }


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.quantite} de {self.matiere_premiere.nom}"

    def json(self):
        return {
            "id": self.id,
            "quantite": self.quantite,
            "matiere_premiere": self.matiere_premiere.json(),
        }


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.IntegerField()
    prix_m2 = models.IntegerField()

    def _str_(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "taxes": self.taxes,
            "prix_m2": self.prix_m2,
        }


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": self.prix,
            "localisation": self.localisation.json(),
        }


class DebitEnergie(models.Model):
    debit = models.IntegerField()
    energie = models.ForeignKey(Energie, on_delete=models.PROTECT)

    def _str_(self):
        return f"{self.debit} ({self.energie.nom})"

    def costs(self):
        return self.debit * self.energie.prix

    def json(self):
        return {
            "id": self.id,
            "debit": self.debit,
            "energie": self.energie.json(),
            "costs": self.costs(),
        }


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)
    surface = models.IntegerField()

    def _str_(self):
        return self.nom

    def costs(self):
        return self.surface * self.localisation.prix_m2

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "surface": self.surface,
            "localisation": self.localisation.json(),
            "costs": self.costs(),
        }


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente = models.IntegerField()
    quantite = models.IntegerField()
    emprise = models.IntegerField()
    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix_de_vente": self.prix_de_vente,
            "quantite": self.quantite,
            "emprise": self.emprise,
            "local": self.local.json(),
        }


class UtilisationMatierePremiere(QuantiteMatierePremiere):
    def json(self):
        return {
            "quantite": self.quantite,
            "matiere_premiere": self.matiere_premiere.json(),
        }


class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)
    prix_unitaire = models.IntegerField()
    delais = models.IntegerField()  # en jours

    def _str_(self):
        return f"{self.quantite} {self.matiere_premiere.nom} (delais {self.delais}j)"

    def costs(self):
        return self.quantite * self.prix_unitaire

    def json(self):
        return {
            "quantite": self.quantite,
            "matiere_premiere": self.matiere_premiere.json(),
            "localisation": self.localisation.json(),
            "prix_unitaire": self.prix_unitaire,
            "delais": self.delais,
            "costs": self.costs(),
        }


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    remuneration = models.IntegerField()

    def _str_(self):
        return self.nom

    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "remuneration": self.remuneration,
        }


class RessourceHumaine(models.Model):
    metier = models.ForeignKey(Metier, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def _str_(self):
        return f"{self.quantite} x {self.metier.nom}"

    def costs(self):
        return self.quantite * self.metier.remuneration

    def json(self):
        return {
            "id": self.id,
            "metier": self.metier.json(),
            "quantite": self.quantite,
            "costs": self.costs(),
        }


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
    cout_maintenance = models.IntegerField()
    operateurs = models.IntegerField()
    debit = models.IntegerField()
    surface = models.IntegerField()
    debit_energie = models.IntegerField()
    taux_utilisation = models.IntegerField()
    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom

    def costs(self):
        return self.cout_maintenance
    def json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix_achat": self.prix_achat,
            "cout_maintenance": self.cout_maintenance,
            "operateurs": self.operateurs,
            "debit": self.debit,
            "surface": self.surface,
            "debit_energie": self.debit_energie,
            "taux_utilisation": self.taux_utilisation,
            "local": self.local.json(),
            "costs": self.costs(),
        }


class Fabrication(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    utilisations_matiere_premiere = models.ManyToManyField(UtilisationMatierePremiere)
    machines = models.ManyToManyField(Machine)
    ressources_humaines = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return f"Fabrication de {self.produit.nom}"

    def json(self):
        return {
            "id": self.id,
            "produit": self.produit.json(),
            "utilisations_matiere_premiere": [
                u.json() for u in self.utilisations_matiere_premiere.all()
            ],
            "machines": [m.json() for m in self.machines.all()],
            "ressources_humaines": [r.json() for r in self.ressources_humaines.all()],
        }
