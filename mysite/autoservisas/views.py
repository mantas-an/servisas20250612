from django.shortcuts import render
from django.http import HttpResponse
from .models import Paslauga, Uzsakymas, UzsakymoEilute, Automobilis, AutomobilioModelis

def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    uzsakymu_kiekis = Uzsakymas.objects.all().count()
    automobiliu_kiekis = Automobilis.objects.all().count()

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,

    }

    return render(request, template_name='autoservisas/index.html', context=context)
