from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_employee, name='create_employee'),
    path('list/', views.get_employees),
    path('external-users/', views.get_external_users),
    path('update/<int:pk>/', views.update_employee),
    path('partial-update/<int:pk>/', views.partial_update_employee),
    path('delete/<int:pk>/', views.delete_employee),
]