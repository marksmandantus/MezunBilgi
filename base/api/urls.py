from django.urls import path
from base.api import views as api_views


urlpatterns = [
    path('persons/', api_views.PersonListCreateAPIView.as_view(), name='person-list'),
    path('persons/<int:pk>/', api_views.PersonDetailAPIView.as_view(), name='person-detail'),
    path('universities/', api_views.UniversityListCreateAPIView.as_view(), name='university-list'),
    path('universities/<int:pk>/', api_views.UniversityDetailAPIView.as_view(), name='university-detail'),
    path('events/', api_views.EventListCreateAPIView.as_view(), name='event-list'),
    path('events/<int:pk>/', api_views.EventDetailAPIView.as_view(), name='event-detail'),
]
