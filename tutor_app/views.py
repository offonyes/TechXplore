from rest_framework import viewsets, permissions, filters
from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination

from tutor_app.models import Tutor
from tutor_app.serializers import TutorSerializer, DetailedTutorSerializer, CreateTutorSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


@extend_schema(tags=['Tutor'], description='Retrieve all tutors',
               parameters=[
                   OpenApiParameter(
                       name='search',
                       type=OpenApiTypes.STR,
                       location=OpenApiParameter.QUERY,
                       description='Filter by city',
                       examples=[
                           OpenApiExample(
                               'Example 1',
                               summary='',
                               value=''
                           ),
                           OpenApiExample(
                               'Example 2',
                               summary='ბათუმი',
                               value='ბათუმი'
                           ),

                       ],
                   ),
                   OpenApiParameter(
                       name='ordering',
                       type=OpenApiTypes.STR,
                       location=OpenApiParameter.QUERY,
                       description='Filter by city',
                       examples=[
                           OpenApiExample(
                               'Example 1',
                               summary='',
                               value=''
                           ),
                           OpenApiExample(
                               'Example 2',
                               summary='subject',
                               value='subject'
                           ),
                            OpenApiExample(
                               'Example 3',
                               summary='month_price',
                               value='month_price'
                           ),
                           OpenApiExample(
                               'Example 4',
                               summary='average_rating',
                               value='average_rating'
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

