from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from report_builder.models import (Report,
                                   Clients, Equipment, OutageType,
                                   Cause, Comment
                                   )


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['clients']

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['equipment']


class OutageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageType
        fields = ['outage_type']


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['causes']


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.C(
    #     slug_field="username", read_only=True, source='auth.Accounts')

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'report',
                  'published',
                  'author', ]


class ReportSerializer(WritableNestedModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.ReadOnlyField(source="auth.Accounts")

    class Meta:
        model = Report
        fields = ['report_type',
                  'noc_ticket',
                  'third_party_ticket',
                  'date_of_outage',
                  'time_of_outage',
                  'notes',
                  'municipalities',
                  'outage_type',
                  'causes',
                  'equipment',
                  'clients',
                  'comments',
                  'author'
                  ]
