from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import CrqAdditionalTaskForm
from .models import CrqAdditionalTask

# Create your views here.
@access_required
def view(request):
	tasks = CrqAdditionalTask.objects.all()
	return render(request, 'crq_additional_tasks/view.html', {'tasks': tasks})


@access_required
def add(request):
	if request.method == 'POST':
		form = CrqAdditionalTaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crq_additional_tasks:view')
	else:
		form = CrqAdditionalTaskForm()
	return render(request, 'crq_additional_tasks/add.html', {'form': form})


@access_required
def edit(request, id):
	task = get_object_or_404(CrqAdditionalTask, id=id)
	if request.method == 'POST':
		form = CrqAdditionalTaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('crq_additional_tasks:view')
	else:
		form = CrqAdditionalTaskForm(instance=task)
	return render(request, 'crq_additional_tasks/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	task = get_object_or_404(CrqAdditionalTask, id=id)
	if request.method == 'POST':
		task.delete()
		return redirect('crq_additional_tasks:view')
	return render(request, 'crq_additional_tasks/delete.html', {'task': task})
