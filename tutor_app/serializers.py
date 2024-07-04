from rest_framework import serializers

from accounts_app.models import CustomUser
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


class RegisterTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['photo', 'city', 'address', 'subject', 'description', 'month_price']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    is_tutor = serializers.BooleanField(write_only=True)
    tutor_details = RegisterTutorSerializer(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'password_confirm', 'is_tutor',
                  'tutor_details']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        is_tutor = validated_data.pop('is_tutor')
        tutor_details = validated_data.pop('tutor_details', None)
        validated_data.pop('password_confirm')

        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()

        if is_tutor and tutor_details:
            Tutor.objects.create(user=user, **tutor_details)

        return user
