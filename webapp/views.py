from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task
from webapp.forms import TaskForm


def task_list_view(request):
    tasks = Task.objects.order_by('status', 'due_date', 'id')
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('task_list'))
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect(reverse('task_list'))
