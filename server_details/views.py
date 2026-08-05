from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import ServerDetailsForm
from .models import ServerDetails

# Create your views here.
@access_required
def view(request):
	servers = ServerDetails.objects.all()
	return render(request, 'server_details/view.html', {'servers': servers})


@access_required
def add(request):
	if request.method == 'POST':
		form = ServerDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('server_details:view')
	else:
		form = ServerDetailsForm()
	return render(request, 'server_details/add.html', {'form': form})


@access_required
def edit(request, id):
	server = get_object_or_404(ServerDetails, id=id)
	if request.method == 'POST':
		form = ServerDetailsForm(request.POST, instance=server)
		if form.is_valid():
			form.save()
			return redirect('server_details:view')
	else:
		form = ServerDetailsForm(instance=server)
	return render(request, 'server_details/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	server = get_object_or_404(ServerDetails, id=id)
	if request.method == 'POST':
		server.delete()
		return redirect('server_details:view')
	return render(request, 'server_details/delete.html', {'server': server})
