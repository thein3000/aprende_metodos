from django.urls import path

from . import views

urlpatterns = [
    path('',views.main_dashboard, name='main_dashboard'),
    path('',views.catalogue_accounts, name='catalogue_accounts'),
    # path('',views.catalogue_categories, name='catalogue_categories'),
    path('movement_data/',views.movement_data, name='movement_data'),
    path('register_income/',views.register_income, name='register_income'),
    path('register_expense/',views.register_expense, name='register_expense'),
    path('register_transfer/',views.register_transfer, name='register_transfer')

]
