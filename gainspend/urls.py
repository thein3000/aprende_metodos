from django.urls import path

from . import views

urlpatterns = [
    # ------------------------------ MOVEMENT -----------------------------------
    path('',views.main_dashboard, name='main_dashboard'),
    path('movement_data/',views.movement_data, name='movement_data'),
    path('register_income/',views.register_income, name='register_income'),
    path('register_expense/',views.register_expense, name='register_expense'),
    path('register_transfer/',views.register_transfer, name='register_transfer'),
    # ------------------------------ ACCOUNT -----------------------------------
    path('account_data/',views.account_data, name='account_data'),
    path('account_catalogue/',views.account_catalogue, name='account_catalogue'),
    path('account_catalogue/<int:field_id>/',views.account_detail,name='account_detail'),
    path('account_catalogue/account_register/',views.account_register, name='account_register'),
    path('account_catalogue/account_delete/<int:field_id>/',views.account_delete, name='account_delete'),
    path('movement_data/<str:account>/',views.account_movement_data, name='account_movement_data'),
    # ------------------------------ CATEGORY -----------------------------------
    # path('',views.catalogue_categories, name='catalogue_categories'),

]
