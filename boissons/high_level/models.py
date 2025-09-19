class QuantiteMatierePremiere(models.Model):
quantite = models.IntegerField()
matiere_premiere = models.ForeignKey(
MatierePremiere,
on_delete=models.PROTECT,
)
class Meta:
abstract = True


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.IntegerField()
    prix_m2 = models.IntegerField()

    def _str_(self):
        return self.nom


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom


class DebitEnergie(models.Model):
    debit = models.ntegerField()
    energie = models.ForeignKey(Energie, on_delete=models.PROTECT)

    def _str_(self):
        return f"{self.debit} ({self.energie.nom})"


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)
    surface = models.integerField()

    def _str_(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente = models.IntegerField()
    quantite = models.IntegerField()
    emprise = models.IntegerField()
    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.IntegerFieldd()

    def _str_(self):
        return self.nom


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT
    )

    class Meta:
        abstract = True  # comme dans ton exemple

    def _str_(self):
        return f"{self.quantite} de {self.matiere_premiere.nom}"


class UtilisationMatierePremiere(QuantiteMatierePremiere):
    # hérite de QuantiteMatierePremiere
    pass


class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    localisation = models.ForeignKey(Localisation, on_delete=models.PROTECT)
    prix_unitaire = models.IntegerField()
    delais = models.IntegerField()  # en jours

    def _str_(self):
        return f"{self.quantite} {self.matiere_premiere.nom} (delais {self.delais}j)"


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    remuneration = models.IntegerField()

    def _str_(self):
        return self.nom


class RessourceHumaine(models.Model):
    metier = models.ForeignKey(Metier, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def _str_(self):
        return f"{self.quantite} x {self.metier.nom}"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
    consommation = models.IntegerField()
    capacite = models.IntegerField()
    emprise = models.IntegerField()
    energie = models.ForeignKey(Energie, on_delete=models.PROTECT)

    def _str_(self):
        return self.nom
