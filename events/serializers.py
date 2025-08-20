from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event, EventRegistration
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data


class EventRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = EventRegistration
        fields = ('id', 'user', 'registered_at', 'is_waitlisted', 'is_active')
        read_only_fields = ('id', 'user', 'registered_at')


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    attendees = UserSerializer(many=True, read_only=True)
    registrations = EventRegistrationSerializer(many=True, read_only=True)
    available_slots = serializers.IntegerField(read_only=True)
    is_full = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Event
        fields = (
            'id', 'title', 'description', 'date_time', 'location',
            'organizer', 'capacity', 'attendees', 'registrations',
            'created_at', 'updated_at', 'is_active', 'available_slots', 'is_full'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'organizer')

    def validate_date_time(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

    def create(self, validated_data):
        # Set the organizer to the current user
        validated_data['organizer'] = self.context['request'].user
        return super().create(validated_data)


class EventRegisterSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    
    def validate(self, data):
        event_id = data.get('event_id')
        user = self.context['request'].user
        
        try:
            event = Event.objects.get(id=event_id, is_active=True)
        except Event.DoesNotExist:
            raise serializers.ValidationError("Event not found or inactive.")
        
        # Check if user is already registered
        if EventRegistration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("You are already registered for this event.")
        
        data['event'] = event
        return data
