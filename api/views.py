from rest_framework import generics
from report_builder.models import *
from rest_framework.response import Response
from api.serializers import *


class ReportListAPIView(generics.ListAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
