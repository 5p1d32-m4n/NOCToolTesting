from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from report_builder.models import (Report,
                                   Clients, Services, OutageType,
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
        model = Services
        fields = ['services']


class OutageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutageType
        fields = ['outage_type']


class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = ['causes']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'report',
                  'author',
                  'published',
                  'parent']

    def get_author(self, obj):
        return obj.author.username


class CommentChildSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'content',
            'id',
            'published']
        read_only_fields = ['author']

    def get_author(self, obj):
        return obj.author.username


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['content',
                  'id',
                  'author',
                  'published',
                  'replies']
        read_only_fields = ['author']

    def get_author(self, obj):
        return obj.author.username

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


class ReportSerializer(WritableNestedModelSerializer):
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
                  'services',
                  'clients',
                  ]
