from __future__ import unicode_literals

from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Identyfikator wyceny")
    first_name = models.CharField(max_length=255, verbose_name="Imię")
    last_name = models.CharField(max_length=255, verbose_name="Nazwisko")
    email_address = models.EmailField(max_length=255, verbose_name="Adres email")
    telephone_number = models.CharField(max_length=255, blank=True, verbose_name="Numer telefonu")
    description = models.TextField(blank=True, verbose_name="Opis")

    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Document(models.Model):
    order = models.ForeignKey(Order, default=None, on_delete=models.CASCADE)
    documents = models.FileField(upload_to='documents/', verbose_name="Plik")

    class Meta:
        verbose_name = "Plik"
        verbose_name_plural = "Pliki"