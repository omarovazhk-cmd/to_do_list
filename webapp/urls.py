from django.urls import path
from webapp.views import task_list_view, task_delete_view

urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('delete/', task_delete_view, name='task_delete'),
]


