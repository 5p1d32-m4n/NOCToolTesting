from report_builder.api.serializers import (
    ClientsSerializer,
    ServicesSerializer,
    OutageTypeSerializer,
    CauseSerializer,
    CommentSerializer,
    ReportSerializer)
from report_builder.models import (
    Equipment,
    Clients,
    OutageType,
    Cause,
    Report,
    Comment)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.db.models import Q
from django.db.models.query import QuerySet


class ReportCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


class CommentListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)


class ComentUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Comment.objects.all()


class ReportDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data)


class ReportUpdateListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        reports = Report.objects.all().exclude(report_type__exact="Final")
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)


class ReportUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Report.objects.all()


class ServicesCreateAPIView(generics.CreateAPIView):
    """
    Serializer for equipment creatino view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Equipment.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetailAPIView(generics.RetrieveAPIView):
    """
    Serializer for equipment detail view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Equipment.objects.all()
    serializer_class = ServicesSerializer


class ServicesListAPIView(APIView):
    """
    Serializer for equipment
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        equipment = Equipment.objects.all()
        serializer = ServicesSerializer(equipment, many=True)
        return Response(serializer.data)


class ServicesUpdateListAPIView(generics.ListAPIView):
    """
    Serializer to list then update equipment.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        equipment = Equipment.objects.all()
        serilizer = ServicesSerializer(equipment, many=True)

        return Response(serilizer.data)


class ServicesUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Serializer Equipment update view.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ServicesSerializer


class ClientsCreateAPIView(generics.CreateAPIView):
    """
    Serializer for clients creatino view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsDetailAPIView(generics.RetrieveAPIView):
    """
    Serializer for clients detail view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsListAPIView(APIView):
    """
    Serializer for clients
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)


class ClientsUpdateListAPIView(generics.ListAPIView):
    """
    Serializer to list then update clients.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        clients = Clients.objects.all()
        serilizer = ClientsSerializer(clients, many=True)

        return Response(serilizer.data)


class ClientsUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Serializer Equipment update view.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ClientsSerializer


class OutageTypeCreateAPIView(generics.CreateAPIView):
    """
    Serializer for outage_type creatino view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = OutageType.objects.all()
    serializer_class = OutageTypeSerializer


class OutageTypeDetailAPIView(generics.RetrieveAPIView):
    """
    Serializer for outage_type detail view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = OutageType.objects.all()
    serializer_class = OutageTypeSerializer


class OutageTypeListAPIView(APIView):
    """
    Serializer for outage_type
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        outage_type = OutageType.objects.all()
        serializer = OutageTypeSerializer(outage_type, many=True)
        return Response(serializer.data)


class OutageTypeUpdateListAPIView(generics.ListAPIView):
    """
    Serializer to list then update outage_type.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        outage_type = OutageType.objects.all()
        serilizer = OutageTypeSerializer(outage_type, many=True)

        return Response(serilizer.data)


class OutageTypeUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Serializer Equipment update view.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = OutageTypeSerializer


class CauseCreateAPIView(generics.CreateAPIView):
    """
    Serializer for cause creatino view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


class CauseDetailAPIView(generics.RetrieveAPIView):
    """
    Serializer for cause detail view
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


class CauseListAPIView(APIView):
    """
    Serializer for cause
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        cause = Cause.objects.all()
        serializer = CauseSerializer(cause, many=True)
        return Response(serializer.data)


class CauseUpdateListAPIView(generics.ListAPIView):
    """
    Serializer to list then update cause.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        cause = Cause.objects.all()
        serilizer = CauseSerializer(cause, many=True)

        return Response(serilizer.data)


class CauseUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Serializer Equipment update view.
    """
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = CauseSerializer
