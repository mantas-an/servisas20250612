from tabnanny import verbose

from django.db import models

class Paslauga(models.Model):
    pavadinimas = models.CharField(
        max_length=100,
        verbose_name="Paslaugos pavadinimas",
        help_text="Iveskite paslaugos pavadinimas"
    )

    def __str__(self):
        return self.pavadinimas

    kaina = models.DecimalField(
        verbose_name="Kaina",
        max_digits=6,
        decimal_places=2,
        default=0.00
    )

class AutomobilioModelis(models.Model):
    marke = models.CharField(
        verbose_name="Automobilio marke",
        max_length=100
    )
    modelis = models.CharField(
        verbose_name="Automobilio modelis",
        max_length=100
    )

class Automobilis(models.Model):
    valstybinis_nr = models.CharField(
        verbose_name="Valsybinis numeris",
        max_length=10
    )
    modelis = models.ForeignKey(
        AutomobilioModelis,
        on_delete=models.SET_NULL,
        null=True
    )

    vin_kodas = models.CharField(
        verbose_name="VIN",
        max_length = 20
    )

    klientas = models.CharField(
        verbose_name="Klientas",
        help_text="Iveskite Fizini ar Juridini asmeni"
    )

class Uzsakymas(models.Model):
    data = models.DateTimeField(
        verbose_name="Uzsakymo data",
        auto_now_add=True

    )

    automobilis = models.ForeignKey(
        Automobilis,
        on_delete=models.SET_NULL,
        null=True
    )




class UzsakymoEilute(models.Model):
    paslauga = models.ForeignKey(
        Paslauga,
        on_delete=models.SET_NULL,
        null=True
    )
    uzsakymas = models.ForeignKey(
        Uzsakymas,
        on_delete=models.SET_NULL,
        null=True
    )
    kiekis = models.IntegerField(
        verbose_name="Kiekis",
        default=1
    )

