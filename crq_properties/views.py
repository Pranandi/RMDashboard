from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import CrqPropertiesForm
from .models import CrqProperties

# Create your views here.
@access_required
def view(request):
	items = CrqProperties.objects.all()
	return render(request, 'crq_properties/view.html', {'items': items})


@access_required
def add(request):
	if request.method == 'POST':
		form = CrqPropertiesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crq_properties:view')
	else:
		form = CrqPropertiesForm()
	return render(request, 'crq_properties/add.html', {'form': form})


@access_required
def edit(request, id):
	item = get_object_or_404(CrqProperties, id=id)
	if request.method == 'POST':
		form = CrqPropertiesForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('crq_properties:view')
	else:
		form = CrqPropertiesForm(instance=item)
	return render(request, 'crq_properties/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	item = get_object_or_404(CrqProperties, id=id)
	if request.method == 'POST':
		item.delete()
		return redirect('crq_properties:view')
	return render(request, 'crq_properties/delete.html', {'item': item})
