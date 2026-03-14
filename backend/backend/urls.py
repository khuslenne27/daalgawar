
from django.urls import path
from appOne import viewshabit
urlpatterns = [
    path('apihabit/', viewshabit.check_service),
]
