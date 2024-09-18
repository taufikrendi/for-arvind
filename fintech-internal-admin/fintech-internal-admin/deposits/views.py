from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.signals import post_save
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from deposits.models import DepositProductMaster
from deposits.signals import create_deposit_product
from deposits.forms import DepositProductForm
from utils.validators import get_user


@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
def all_deposit_product(request):
    data = DepositProductMaster.objects.using('funds_slave').all()

    search = request.POST.get('search')

    if search:
        data = data.filter(Q(email__contains=search))
    else:
        data.using('funds_slave')

    page = request.GET.get('page', 1)
    paginator = Paginator(data.using('funds_slave'), 25)

    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    context = {'data_list': data_list}

    return render(request, 'registration/administrations/deposit/all_deposit.html', context)


@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
def edit_deposit_product(request, id):
    if not get_user(request):
        raise Http404
    data_values = DepositProductMaster.objects.using('funds_master').filter(
        deposit_product_master_id=id
    )
    if request.method == 'POST':
        form = DepositProductForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = get_user(request)
            data.name = form.cleaned_data.get('name')
            data.revenue = form.cleaned_data.get('revenue')
            data.description = form.cleaned_data.get('description')
            data.minimum_value = form.cleaned_data.get('minimum_amount')
            data.type = True if form.cleaned_data.get('type') == 'Fluctuate.TR' else False
            data_values.update(
                deposit_product_master_name=data.name,
                deposit_product_master_description=data.description,
                deposit_product_active=True,
                deposit_product_master_revenue_share=data.revenue,
                deposit_product_minimum_fluctuate_revenue=data.type,
                deposit_product_minimum_amount=data.minimum_value,
                deposit_product_master_created_by=data.user,
            )
            messages.success(request, 'Data Berhasil Disimpan!')
            return redirect('deposits:all-deposit-product')
        else:
            messages.error(request, 'Error Pada Field Ini!')
    else:
        form = DepositProductForm()
    context = {
        'form': form,
        'data': data_values
    }
    return render(request, 'registration/administrations/deposit/edit_deposit.html', context)


@csrf_protect
@login_required(login_url=settings.LOGIN_URL)
def add_deposit_product(request):
    if not get_user(request):
        raise Http404

    if request.method == 'POST':
        form = DepositProductForm(request.POST)
        if form.is_valid():
            post_save.disconnect(create_deposit_product)
            data = form.save(commit=False)
            data.user = get_user(request)
            data.name = form.cleaned_data.get('name')
            data.revenue = form.cleaned_data.get('revenue')
            data.minimum_value = form.cleaned_data.get('minimum_amount')
            data.type = True if form.cleaned_data.get('type') == 'Fluctuate.TR' else False
            data.description = form.cleaned_data.get('description')
            post_save.send(sender=DepositProductMaster, created=None, instance=data,
                           dispatch_uid="create_deposit_product")
            messages.success(request, 'Data Berhasil Disimpan!')
            return redirect('deposits:all-deposit-product')
        else:
            messages.error(request, 'Error Pada Field Ini!')
    else:
        form = DepositProductForm()
    return render(request, 'registration/administrations/deposit/add_deposit.html', {'form': form})
