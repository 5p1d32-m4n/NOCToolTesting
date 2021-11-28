from django.db import models
from datetime import date
from users.models import CustomUser


class Services(models.Model):
    services = models.CharField(max_length=50, primary_key=False)

    def __str__(self):
        return f'Servicio: {self.services}'

    class Meta:
        verbose_name_plural = 'Services'


class Clients(models.Model):
    clients = models.CharField(max_length=50)

    def __str__(self):
        return f'Cliente: {self.clients}'

    class Meta:
        verbose_name_plural = 'Clients'


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
        ("Finalizado", "Finalizado")
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

    outage_type = models.CharField(blank=True, default=None, max_length=250,
                                   null=True)
    causes = models.CharField(blank=True, default=None, max_length=250,
                              null=True)
    services = models.JSONField(default=dict)
    clients = models.JSONField(default=dict)

    def __str__(self):
        return f'Evento: {self.noc_ticket}, en la fecha {self.date_of_outage}'


# class CommentManager(models.Manager):
#     def all(self):
#         qs = super(CommentManager, self).filter(parent=None)
#         return qs


class Comment(models.Model):
    content = models.TextField(max_length=255)
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, null=True, blank=True,
        related_name='comments')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    published = models.DateField(auto_now=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    # objects = CommentManager()

    def __str__(self):
        return f'Comment by: {self.author}; on report: {self.report}'

    class Meta:
        ordering = ("published",)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-published').all()

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
