from django.urls import path
from base.api import views as api_views


urlpatterns = [
    path('persons/', api_views.person_list_create_api_view, name='person-list'),
    path('persons/<int:pk>/', api_views.person_detail_api_view, name='person-detail'),
]
