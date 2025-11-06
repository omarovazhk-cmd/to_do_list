from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task


def task_list_view(request):
    tasks = Task.objects.order_by('status', 'due_date', 'id')
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create_view(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date') or None

        if description:
            Task.objects.create(
                description=description,
                status=status,
                due_date=due_date
            )
        return redirect('task_list')

    return render(request, 'task_create.html')


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'task_confirm_delete.html', {'task': task})


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.due_date = request.POST.get('due_date') or None
        if hasattr(task, 'description_detail'):
            task.description_detail = request.POST.get('description_detail') or ''
        task.save()
        return redirect('task_detail', pk=task.pk)

    return render(request, 'task_edit.html', {'task': task})
