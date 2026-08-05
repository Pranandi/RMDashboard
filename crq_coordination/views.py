from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import CrqCoordinationForm
from .models import CrqCoordination


@access_required
def view(request):
	items = CrqCoordination.objects.all()
	return render(request, 'crq_coordination/view.html', {'items': items})


@access_required
def add(request):
	if request.method == 'POST':
		form = CrqCoordinationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crq_coordination:view')
	else:
		form = CrqCoordinationForm()
	return render(request, 'crq_coordination/add.html', {'form': form})


@access_required
def edit(request, id):
	item = get_object_or_404(CrqCoordination, id=id)
	if request.method == 'POST':
		form = CrqCoordinationForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('crq_coordination:view')
	else:
		form = CrqCoordinationForm(instance=item)
	return render(request, 'crq_coordination/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	item = get_object_or_404(CrqCoordination, id=id)
	if request.method == 'POST':
		item.delete()
		return redirect('crq_coordination:view')
	return render(request, 'crq_coordination/delete.html', {'item': item})
