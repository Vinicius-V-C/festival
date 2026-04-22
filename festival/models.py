from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def str(self):
        return self.nome



class Palco(models.Model):
    nome = models.CharField(max_length=100)

    def str(self):
        return self.nome



class Dia(models.Model):
    data = models.DateField()

    def str(self):
        return str(self.data)



class Concerto(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="concertos")
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name="concertos")
    hora = models.TimeField()
    palco = models.ForeignKey(Palco, on_delete=models.CASCADE, related_name="concertos")

    def str(self):
        return f"{self.banda} - {self.dia}"