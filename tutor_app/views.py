from rest_framework import viewsets, permissions, filters
from drf_spectacular.utils import extend_schema

from tutor_app.models import Tutor
from tutor_app.serializers import TutorSerializer, DetailedTutorSerializer, CreateTutorSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


@extend_schema(tags=['Tutor'], description='Retrieve all tutors',
               parameters=[
                   # OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str),
                   OpenApiParameter(
                       name='search',
                       type=OpenApiTypes.STR,
                       location=OpenApiParameter.QUERY,
                       description='Filter by city',
                       examples=[
                           OpenApiExample(
                               'Example 1',
                               summary='City1',
                               value='თბილისი'
                           ),
                           OpenApiExample(
                               'Example 2',
                               summary='City 2',
                               value='ბათუმი'
                           ),

                       ],
                   ),
               ],
               )
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering = ['id']
    search_fields = ['subject', 'city',]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedTutorSerializer
        if self.action == 'list':
            return TutorSerializer
        return CreateTutorSerializer

    def get_queryset(self):
        return Tutor.objects.select_related('user')

