from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Event, EventRegistration
from .serializers import (
    UserSerializer, CustomTokenObtainPairSerializer,
    EventSerializer, EventRegisterSerializer, EventRegistrationSerializer
)


class UserCreateView(generics.CreateAPIView):
    """View for user registration."""
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    """View for obtaining JWT tokens."""
    serializer_class = CustomTokenObtainPairSerializer


class EventListCreateView(generics.ListCreateAPIView):
    """View for listing and creating events."""
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.filter(is_active=True)
        
        # Filter by upcoming events
        upcoming = self.request.query_params.get('upcoming', None)
        if upcoming and upcoming.lower() == 'true':
            queryset = queryset.filter(date_time__gte=timezone.now())
            
        # Filter by organizer
        organizer = self.request.query_params.get('organizer', None)
        if organizer:
            queryset = queryset.filter(organizer__username=organizer)
            
        # Search by title or location
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                models.Q(title__icontains=search) | 
                models.Q(location__icontains=search)
            )
            
        return queryset.order_by('date_time')


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a single event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_destroy(self, instance):
        # Soft delete
        instance.is_active = False
        instance.save()


class EventRegisterView(APIView):
    """View for registering to an event."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EventRegisterSerializer(
            data=request.data,
            context={'request': request}
        )
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        event = serializer.validated_data['event']
        user = request.user
        
        # Check if event is full
        if event.is_full:
            # Add to waitlist
            registration = EventRegistration.objects.create(
                user=user,
                event=event,
                is_waitlisted=True
            )
            return Response(
                {"detail": "Event is full. You have been added to the waitlist."},
                status=status.HTTP_202_ACCEPTED
            )
        else:
            # Register for the event
            registration = EventRegistration.objects.create(
                user=user,
                event=event
            )
            event.attendees.add(user)
            return Response(
                {"detail": "Successfully registered for the event."},
                status=status.HTTP_201_CREATED
            )


class UserRegisteredEventsView(generics.ListAPIView):
    """View for listing events the current user is registered for."""
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(
            registrations__user=self.request.user,
            registrations__is_active=True,
            is_active=True
        ).order_by('date_time')


class UserOrganizedEventsView(generics.ListAPIView):
    """View for listing events organized by the current user."""
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Event.objects.filter(
            organizer=self.request.user,
            is_active=True
        ).order_by('date_time')
