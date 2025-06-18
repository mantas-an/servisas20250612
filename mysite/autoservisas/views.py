from django.shortcuts import render
from django.http import HttpResponse
from .models import Paslauga, Uzsakymas, UzsakymoEilute, Automobilis, AutomobilioModelis

def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    atliktu_uzsakymu = Uzsakymas.objects.filter(status__exact = 'a').count()
    automobiliu_kiekis = Automobilis.objects.all().count()

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'atliktu_uzsakymu': atliktu_uzsakymu,
        'automobiliu_kiekis': automobiliu_kiekis,

    }

    return render(request, template_name='autoservisas/index.html', context=context)
