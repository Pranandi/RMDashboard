from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import UploaderVariantForm
from .models import UploaderVariant


@access_required
def view(request):
    items = UploaderVariant.objects.all()
    return render(request, 'uploader_variants/view.html', {'items': items})


@access_required
def add(request):
    if request.method == 'POST':
        form = UploaderVariantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uploader_variants:view')
    else:
        form = UploaderVariantForm()
    return render(request, 'uploader_variants/add.html', {'form': form})


@access_required
def edit(request, id):
    item = get_object_or_404(UploaderVariant, id=id)
    if request.method == 'POST':
        form = UploaderVariantForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('uploader_variants:view')
    else:
        form = UploaderVariantForm(instance=item)
    return render(request, 'uploader_variants/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
    item = get_object_or_404(UploaderVariant, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('uploader_variants:view')
    return render(request, 'uploader_variants/delete.html', {'item': item})
