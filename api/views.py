from rest_framework import generics
from report_builder.models import (Services,
                                   #    ServiceAmount,
                                   Clients,
                                   #    ClientAmount,
                                   OutageType,
                                   Cause,
                                   Report)
# from rest_framework.response import Response
from api.serializers import (ClientsSerializer,
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


class ReportListAPIView(generics.ListAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
