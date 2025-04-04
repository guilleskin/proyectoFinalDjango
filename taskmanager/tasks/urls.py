from django.urls import path
from . import views  

urlpatterns = [
    path('', views.task_list, name='home'),  # ← Agregamos el nombre 'home'
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('create/', views.task_create, name='task_create'),
    path('<int:task_id>/update/', views.task_update, name='task_update'),
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('', views.task_list, name='task_list'),  # Cambiamos el nombre de 'home' a 'task_list'
    path('register/', views.register, name='register'),



]
