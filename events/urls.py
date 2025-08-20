from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = 'events'

urlpatterns = [
    # Authentication
    path('auth/register/', views.UserCreateView.as_view(), name='user-register'),
    path('auth/token/', views.CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    # Events
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyView.as_view(), 
         name='event-retrieve-update-destroy'),
    path('events/<int:pk>/register/', views.EventRegisterView.as_view(), 
         name='event-register'),
    
    # User-specific endpoints
    path('users/me/events/registered/', views.UserRegisteredEventsView.as_view(), 
         name='user-registered-events'),
    path('users/me/events/organized/', views.UserOrganizedEventsView.as_view(), 
         name='user-organized-events'),
]
