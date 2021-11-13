from django.db import models

class stabile(models.Model):
    facility_manager = models.CharField(max_length=64)
    nome_stabile = models.CharField(max_length=64)
    indirizzo = models.CharField(max_length=64)
    data_aggiunta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "stabili"

    def __str__(self):
        return f"{self.nome_stabile} - {self.indirizzo}"


# Create your models here.
class scena(models.Model):
    stabile = models.ForeignKey(stabile, on_delete=models.CASCADE)
    scena = models.CharField(max_length=64)
    tipo_di_impianto = models.CharField(max_length=64) #models.IntegerField()

    class Meta:
        verbose_name_plural = "scene"
    def __str__(self):
        return f"{self.stabile} ({self.scena})"

class componente(models.Model):
    scena = models.ForeignKey(scena, on_delete=models.CASCADE)
    codice = models.CharField(max_length=64)
    modello = models.CharField(max_length=64)
    data_aggiunta = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "componenti"

    def __str__(self):
        return f"{self.scena} - {self.modello}"


class manutenzione(models.Model):
    scena = models.ForeignKey(scena, on_delete=models.CASCADE)
    descrizione = models.CharField(max_length=64)
    manutentore = models.CharField(max_length=64)
    data_aggiunta = models.DateTimeField(auto_now_add=True)
    è_richiesta_iniziale = models.BooleanField()

    class Meta:
        verbose_name_plural = "manutenzioni"

    def __str__(self):
        return f"{self.scena} - {self.manutentore}"

