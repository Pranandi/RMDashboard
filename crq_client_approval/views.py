from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from .forms import CrqClientApprovalForm
from .models import CrqClientApproval

# Create your views here.
@access_required
def view(request):
	approvals = CrqClientApproval.objects.all()
	return render(request, 'crq_client_approval/view.html', {'approvals': approvals})


@access_required
def add(request):
	if request.method == 'POST':
		form = CrqClientApprovalForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crq_client_approval:view')
	else:
		form = CrqClientApprovalForm()
	return render(request, 'crq_client_approval/add.html', {'form': form})


@access_required
def edit(request, id):
	approval = get_object_or_404(CrqClientApproval, id=id)
	if request.method == 'POST':
		form = CrqClientApprovalForm(request.POST, instance=approval)
		if form.is_valid():
			form.save()
			return redirect('crq_client_approval:view')
	else:
		form = CrqClientApprovalForm(instance=approval)
	return render(request, 'crq_client_approval/edit.html', {'form': form, 'id': id})


@access_required
def delete(request, id):
	approval = get_object_or_404(CrqClientApproval, id=id)
	if request.method == 'POST':
		approval.delete()
		return redirect('crq_client_approval:view')
	return render(request, 'crq_client_approval/delete.html', {'approval': approval})
