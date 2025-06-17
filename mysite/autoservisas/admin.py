from django.contrib import admin
from .models import AutomobilioModelis, Paslauga, Automobilis, Uzsakymas, UzsakymoEilute

class UzsakymoEiluteInLine(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0


class UzsakymaiAdmin(admin.ModelAdmin):
    list_display = ['automobilis', 'data', 'visa_suma', 'status'] #PRIDETI 'visa_suma' kai funkcija sutvarkysiu
    inlines = [UzsakymoEiluteInLine]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ['klientas', 'modelis', 'valstybinis_nr', "vin_kodas"]
    list_filter = ['klientas', 'modelis']
    search_fields = ['valstybinis_nr', 'vin_kodas']


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ['pavadinimas', 'kaina']




admin.site.register(AutomobilioModelis)
admin.site.register(Paslauga,PaslaugaAdmin)
admin.site.register(Automobilis,AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymaiAdmin)
admin.site.register(UzsakymoEilute)




