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
        due_date = request.POST.get('due_date')

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
    return redirect(reverse('task_list'))
