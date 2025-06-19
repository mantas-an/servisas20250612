from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paslauga, Uzsakymas, UzsakymoEilute, Automobilis, AutomobilioModelis
from django.views import generic

def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    atliktu_uzsakymu = Uzsakymas.objects.filter(status__exact = 'a').count()
    automobiliu_kiekis = Automobilis.objects.all().count()
    uzsakymai = Uzsakymas.objects.all().count()

    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'atliktu_uzsakymu': atliktu_uzsakymu,
        'automobiliu_kiekis': automobiliu_kiekis,
        'uzsakymai': uzsakymai,

    }

    return render(request, template_name='autoservisas/index.html', context=context)


def automobiliai(request):

    automobiliai = Automobilis.objects.all()
    paginator = Paginator(automobiliai, per_page=2)
    page_number = request.GET.get('page')
    paged_automobiliai = paginator.get_page(page_number)

    context = {
        'automobiliai': paged_automobiliai,

    }
    # print(automobiliai)

    return render(request, template_name='autoservisas/automobiliai.html', context = context)

def automobilis(request, automobilio_id):
    automobilis = Automobilis.objects.get(pk = automobilio_id)

    context = {
        'automobilis':automobilis
    }

    return render(request, template_name="autoservisas/automobilis.html", context = context)

class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    template_name = "autoservisas/uzsakymai.html"
    context_object_name = "uzsakymai"
    paginate_by = 3

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = "autoservisas/uzsakymas.html"
    context_object_name = "uzsakymas"
