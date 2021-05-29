from django.db import models
from datetime import date, time
from django.db.models.expressions import F


class Services(models.Model):
    services = models.CharField(max_length=50)

    def __str__(self):
        return f'Servicios afectados: {self.services}'


class ServiceAmount(models.Model):
    service_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Cantidad de servicios afectados: {self.service_amount}'


class Clients(models.Model):
    clients = models.CharField(max_length=50)

    def __str__(self):
        return f'Clientes afectados: {self.clients}'


class ClientAmount(models.Model):
    client_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Cantidad de clientes afectados: {self.client_amount}'


class OutageType(models.Model):
    outage_type = models.CharField(max_length=50)

    def __str__(self):
        return f'Tipo de averia: {self.outage_type}'


class Cause(models.Model):
    causes = models.CharField(max_length=50)

    def __str__(self):
        return f'Causa de averia: {self.causes}'


class Report(models.Model):
    STATES = (
        ("Inicial", "Inicial"),
        ("Actualizacion", "Actualizacion"),
        ("Final", "Final")
    )

    report_type = models.CharField(max_length=15, choices=STATES, default=None)
    noc_ticket = models.CharField(
        max_length=15, primary_key=True, unique=True, default=None)
    third_party_ticket = models.CharField(
        max_length=15, unique=True, blank=True)
    date_of_outage = models.DateField(
        verbose_name='Fecha de Evento', default=date.today)
    time_of_outage = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, editable=True)
    notes = models.TextField(blank=True, null=True, max_length=500)
    municipalities = models.CharField(max_length=200)

    """
    Foreign Keys
    """

    services = models.ManyToManyField(Services, blank=True)
    service_amount = models.ManyToManyField(ServiceAmount, blank=True)
    clients = models.ManyToManyField(Clients, blank=True)
    client_amount = models.ManyToManyField(ClientAmount, blank=True)
    outage_type = models.ManyToManyField(OutageType, blank=True)
    cause = models.ManyToManyField(Cause, blank=True)

    def __str__(self):
        return f'Evento: {self.noc_ticket}, en la fecha {self.date_of_outage}'
