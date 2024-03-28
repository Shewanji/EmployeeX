from django.urls import path

from . import views

app_name = 'myApp'

urlpatterns = [
        path("", views.home, name="home"),
        path('login/', views.user_login, name='user_login'),
        path('signup/', views.signup, name='signup'),
        path('logout/', views.user_logout, name='user_logout'),
        path('create/', views.create_employee, name='create_employee'),
        path('list/', views.employee_list, name='employee_list'),
        path('<int:pk>/', views.employee_detail, name='employee_detail'),
        path('<int:pk>/update/', views.update_employee, name='update_employee'),
        path('<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]
