from django.urls import path
from webapp.views import task_list_view, task_create_view, task_delete_view, task_detail_view

urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('create/', task_create_view, name='task_create'),
    path('delete/<int:pk>/', task_delete_view, name='task_delete'),
    path('task/<int:pk>/', task_detail_view, name='task_detail'),
]


