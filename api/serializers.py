from rest_framework import serializers
from report_builder.models import (
    Report, Clients, ClientAmount, Services, ServiceAmount, OutageType, Cause)


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['clients']

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)


class ClientAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAmount
        fields = ['client_amount']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services']


class ServiceAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAmount
        fields = ['service_amount']


class OutageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageType
        fields = ['outage_type']


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['causes']


class ReportSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True)
    service_amount = ServiceAmountSerializer(many=True)
    clients = ClientsSerializer(many=True)
    client_amount = ClientAmountSerializer(many=True)
    outage_type = OutageTypeSerializer(many=True)
    causes = CauseSerializer(many=True)

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
                  'causes']

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        service_amount_data = validated_data.pop('service_amount')
        clients_data = validated_data.pop('clients')
        client_amount_data = validated_data.pop('client_amount')
        outage_type_data = validated_data.pop('outage_type')
        causes_data = validated_data.pop('causes')

        report = Report.objects.create(**validated_data)

        for data in services_data:
            service = Services.objects.create(**data)
            report.services.add(service)
        for data in service_amount_data:
            service_amount = ServiceAmount.objects.create(
                **data)
            report.service_amount.add(service_amount)
        for data in clients_data:
            clients = Clients.objects.create(**data)
            report.clients.add(clients)
        for data in client_amount_data:
            client_amount = ClientAmount.objects.create(**data)
            report.client_amount.add(client_amount)
        for data in outage_type_data:
            outage_type = OutageType.objects.create(**data)
            report.outage_type.add(outage_type)
        for data in causes_data:
            causes = Cause.objects.create(**data)
            report.causes.add(causes)

        return report
