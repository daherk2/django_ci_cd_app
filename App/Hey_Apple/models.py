from django.db import models

# Create your models here.

class Documento(models.Model):

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    opcoes = [("balancete","balancete"),
        ("LRF", "LRF"),
        ("Receita_Corrente_Liquida", "Receita_Corrente_Liquida"),
        ("Cargos_e_Salarios", "Cargos_e_Salarios"),
        ("LOA_2018","LOA_2018"),
        ("PPA_2018_a_2021","PPA_2018_a_2021"),
        ("Teste_de_App","Teste_de_App")]

    tipo = models.TextField(max_length=200, blank=False, null=False, choices=opcoes)
    nome = models.TextField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(upload_to="teste")

    def __str__(self):
        return str(self.nome)