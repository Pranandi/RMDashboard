from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import DcRegionForm
from .models import DcRegion


@access_required
def view(request):
	items = DcRegion.objects.all()
	return render(request, 'dc_region/view.html', {'items': items})


@access_required
def add(request):
	if request.method == 'POST':
		form = DcRegionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dc_region:view')
	else:
		form = DcRegionForm()
	return render(request, 'dc_region/add.html', {'form': form})


@access_required
def edit(request, id):
	item = get_object_or_404(DcRegion, id=id)
	if request.method == 'POST':
		form = DcRegionForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('dc_region:view')
	else:
		form = DcRegionForm(instance=item)
	return render(request, 'dc_region/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	item = get_object_or_404(DcRegion, id=id)
	if request.method == 'POST':
		item.delete()
		return redirect('dc_region:view')
	return render(request, 'dc_region/delete.html', {'item': item})
