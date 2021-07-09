from rest_framework import generics, viewsets

from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from report_builder.models import (
    Services,
    #    ServiceAmount,
    Clients,
    #    ClientAmount,
    OutageType,
    Cause,
    Report)
# from rest_framework.response import Response
from report_builder.api.serializers import (
    ClientsSerializer,
    #  ClientAmountSerializer,
    ServicesSerializer,
    #  ServiceAmountSerializer,
    OutageTypeSerializer,
    CauseSerializer,
    ReportSerializer)


class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailAPIView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportListAPIView(APIView):

    # queryset = Report.objects.all()
    # serializer_class = ReportSerializer

    def get(self, request, format=None):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data)


class ReportUpdateListAPIView(generics.ListAPIView):
    # unfiltered = Report.objects.all()
    # filtered = unfiltered.exclude(report_type__exact="Final")
    # queryset = filtered
    # serializer_class = ReportSerializer
    def get(self, request, format=None):
        reports = Report.objects.all().exclude(report_type__exact="Final")
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)


class ReportUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ReportSerializer
