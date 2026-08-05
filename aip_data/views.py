from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404  # type: ignore

from Main.auth_utils import access_required
from Main.csv_utils import write_csv_row
from .forms import AipDataForm
from .models import AipData

@access_required
def view(request):
    #items = AipData.objects.all()[:20]  # Limit to 20 records for performance
    return render(request, 'aip_data/view.html')

@access_required
def add(request):
    if request.method == 'POST':
        form = AipDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aip_data:view')
    else:
        form = AipDataForm()
    return render(request, 'aip_data/add.html', {'form': form})

@access_required
def edit(request, id):
    item = get_object_or_404(AipData, id=id)
    if request.method == 'POST':
        form = AipDataForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('aip_data:view')
    else:
        form = AipDataForm(instance=item)
    return render(request, 'aip_data/edit.html', {'form': form, 'id': id})

@access_required
def delete(request, id):
    item = get_object_or_404(AipData, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('aip_data:view')
    return render(request, 'aip_data/delete.html', {'item': item})

#@access_required
def ajax_table(request):
    # This view will be called by DataTables for server-side processing
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')
    order_column = request.GET.get('order[0][column]', '0')
    order_dir = request.GET.get('order[0][dir]', 'asc')
    print(request.get_full_path())
    queryset = AipData.objects.all()

    if search_value:
        queryset = queryset.filter(
            Q(server__icontains=search_value) |
            Q(inst_comp_name__icontains=search_value) |
            Q(primary_ip__icontains=search_value) |
            Q(inst_comp_status__icontains=search_value) |
            Q(aip_status__icontains=search_value) |
            Q(vpdc_profile__icontains=search_value) |
            Q(customer_site_id__icontains=search_value) |
            Q(customer_site_name__icontains=search_value) |
            Q(rank__icontains=search_value) |
            Q(physical_site_id__icontains=search_value) |
            Q(support_region__icontains=search_value) |
            Q(sales_product_line__icontains=search_value) |
            Q(service_package__icontains=search_value)
        )

    total_records = queryset.count()
    queryset = queryset[start:start + length]

    data = []
    for i, item in enumerate(queryset, start=1):
        j=start + i
        row = []
        if request.session.get('can_edit') or request.session.get('can_delete'):
            actions = ''
            if request.session.get('can_edit'):
                actions += f'<a href="/aip-data/edit/{item.id}/" class="btn btn-primary btn-sm">Edit</a> '
            if request.session.get('can_delete'):
                actions += f'<a href="/aip-data/delete/{item.id}/" class="btn btn-danger btn-sm">Delete</a>'
            row = [actions]
            
        row += [
            
            j,
            item.server,
            item.inst_comp_name,
            item.primary_ip,
            item.inst_comp_status,
            item.aip_status,
            item.vpdc_profile,
            item.customer_site_id,
            item.customer_site_name,
            item.rank,
            item.physical_site_id,
            item.support_region,
            item.sales_product_line,
            item.service_package
        ]
        data.append(row)

    return JsonResponse({
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': total_records,
        'data': data
    })

@access_required
def export(request):
    import csv
    from django.http import HttpResponse # type: ignore
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AipData.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Server', 'Inst Comp Name', 'Primary IP', 'Inst Comp Status', 'AIP Status', 'VPDC Profile', 'Customer Site ID', 'Customer Site Name', 'Rank', 'Physical Site ID', 'Support Region', 'Sales Product Line', 'Service Package'])
    aip_data = AipData.objects.all()
    for i, v in enumerate(aip_data, start=1):
        write_csv_row(writer, [i, v.server, v.inst_comp_name, v.primary_ip, v.inst_comp_status, v.aip_status, v.vpdc_profile, v.customer_site_id, v.customer_site_name, v.rank, v.physical_site_id, v.support_region, v.sales_product_line, v.service_package])
    return response
