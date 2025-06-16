

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

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

class AutomobilioModelis(models.Model):
    marke = models.CharField(
        verbose_name="Automobilio marke",
        max_length=100
    )
    modelis = models.CharField(
        verbose_name="Automobilio modelis",
        max_length=100
    )

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobiliu modeliai"

    def __str__(self):
        return f'{self.modelis}, {self.marke}'


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

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def __str__(self):
        return f' {self.modelis}, ({self.valstybinis_nr})'


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


    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymai"



    def __str__(self):
        return f'{self.data}, {self.automobilis}'




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




    class Meta:
        verbose_name = "Uzsakymo eilute"
        verbose_name_plural = "Uzsakymo eilutes"



    def __str__(self):
        return f' {self.paslauga} '








