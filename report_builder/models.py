from django.db import models
from datetime import date
from users.models import CustomUser


class Services(models.Model):
    services = models.CharField(max_length=50, primary_key=False)

    def __str__(self):
        return f'Servicio: {self.services}'


class Clients(models.Model):
    clients = models.CharField(max_length=50)

    def __str__(self):
        return f'Cliente: {self.clients}'


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
        ("Actualización", "Actualización"),
        ("Final", "Final")
    )
    # Unique per report fields
    report_type = models.CharField(max_length=15, choices=STATES, default=None)
    noc_ticket = models.CharField(
        max_length=15, primary_key=True, unique=True, default=None)
    third_party_ticket = models.CharField(
        max_length=15, unique=True, blank=True, null=True)
    date_of_outage = models.DateField(
        verbose_name='Fecha de Evento', default=date.today)
    time_of_outage = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, editable=True)
    notes = models.TextField(blank=True, null=True, max_length=500)
    municipalities = models.CharField(max_length=200)

    # Repeatedly used fields.
    # TODO: Deprecate these fields.
    # services = models.CharField(blank=True, default=None, max_length=250,
    #                             null=True)
    # service_amount = models.CharField(blank=True, default="0",max_length=250,
    #                                   null=True)
    # clients = models.CharField(blank=True, default=None, max_length=250,
    #                            null=True)
    # client_amount = models.CharField(blank=True, default="0", max_length=250,
    #                                  null=True)
    outage_type = models.CharField(blank=True, default=None, max_length=250,
                                   null=True)
    causes = models.CharField(blank=True, default=None, max_length=250,
                              null=True)
    # Testing Json fileds
    services = models.JSONField(default=dict)
    clients = models.JSONField(default=dict)

    def __str__(self):
        return f'Evento: {self.noc_ticket}, en la fecha {self.date_of_outage}'


class Comment(models.Model):
    comment = models.TextField()
    report = models.ForeignKey(
        Report, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.comment}'
