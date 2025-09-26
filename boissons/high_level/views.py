# Create your views here.

from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .models import (
    MatierePremiere,
    Localisation,
    Energie,
    DebitEnergie,
    Local,
    Produit,
    UtilisationMatierePremiere,
    ApprovisionnementMatierePremiere,
    Metier,
    RessourceHumaine,
    Machine,
    Fabrication,
)


class JSONDetailView(DetailView):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class MatierePremiereDetailView(JSONDetailView):
    model = MatierePremiere


class LocalisationDetailView(JSONDetailView):
    model = Localisation


class EnergieDetailView(JSONDetailView):
    model = Energie


class DebitEnergieDetailView(JSONDetailView):
    model = DebitEnergie


class LocalDetailView(JSONDetailView):
    model = Local


class ProduitDetailView(JSONDetailView):
    model = Produit


class UtilisationMatierePremiereDetailView(JSONDetailView):
    model = UtilisationMatierePremiere


class ApprovisionnementMatierePremiereDetailView(JSONDetailView):
    model = ApprovisionnementMatierePremiere


class MetierDetailView(JSONDetailView):
    model = Metier


class RessourceHumaineDetailView(JSONDetailView):
    model = RessourceHumaine


class FabricationDetailView(JSONDetailView):
    model = Fabrication


class MachineDetailView(JSONDetailView):
    model = Machine
