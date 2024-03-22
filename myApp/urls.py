from django.urls import path

from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path('employee/create/', views.create_employee, name='create_employee'),
        path('employee/list/', views.employee_list, name='employee_list'),
        path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
        path('employee/<int:pk>/update/', views.update_employee, name='update_employee'),
        path('employee/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]
