from django.urls import path

from . import views

urlpatterns = [
    path('',views.main_dashboard, name='main_dashboard'),
    path('movement_data/',views.movement_data, name='movement_data'),
]
