from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from report_builder.models import (Report,
                                   Clients, Services, OutageType, Cause,
                                   #    ClientAmount, ServiceAmount,
                                   )


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['clients', 'client_amount']

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)


# class ClientAmountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientAmount
#         fields = ['client_amount']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services', 'service_amount']


# class ServiceAmountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceAmount
#         fields = ['service_amount']


class OutageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageType
        fields = ['outage_type']


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['causes']


class ReportSerializer(WritableNestedModelSerializer):
    services = ServicesSerializer(many=True)
    # service_amount = ServiceAmountSerializer(many=True)
    clients = ClientsSerializer(many=True)
    # client_amount = ClientAmountSerializer(many=True)
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
                  #   'service_amount',
                  'clients',
                  #   'client_amount',
                  'outage_type',
                  'causes']
