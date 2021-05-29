from rest_framework import serializers
from report_builder.models import (
    Report, Clients, ClientAmount, Services, ServiceAmount, OutageType, Cause)


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class ClientAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAmount
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class ServiceAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAmount
        fields = "__all__"


class OutageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageType
        fields = "__all__"


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True, read_only=True)
    service_amount = ServiceAmountSerializer(many=True, read_only=True)
    clients = ClientsSerializer(many=True, read_only=True)
    client_amount = ClientAmountSerializer(many=True, read_only=True)
    outage_type = OutageTypeSerializer(many=True, read_only=True)
    cause = CauseSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = ['report_type',
                  'noc_ticket',
                  'third_party_ticket',
                  'date_of_outage',
                  'time_of_outage',
                  'notes',
                  'municipalities',
                  'services',
                  'service_amount',
                  'clients',
                  'client_amount',
                  'outage_type',
                  'cause']
