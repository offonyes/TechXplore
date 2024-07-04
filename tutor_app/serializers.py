from rest_framework import serializers

from tutor_app.views import Tutor
from accounts_app.serializers import CustomUserSerializer, DetailedCustomUserSerializer


class TutorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Tutor
        fields = ['id', 'user', 'city', 'subject', 'month_price', 'average_rating', 'photo']


class DetailedTutorSerializer(serializers.ModelSerializer):
    user = DetailedCustomUserSerializer()

    class Meta:
        model = Tutor
        fields = '__all__'


class CreateTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
