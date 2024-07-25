from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages


from .models import Device, DeviceList, Transaction
from .forms import DeviceForm

def home(request):
    devices = Device.objects.all()  # Show all devices on the home page
    return render(request, 'cashify_app/index.html', {'devices': devices})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cashify_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('device_list')
    else:
        form = AuthenticationForm()
    return render(request, 'cashify_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def device_list_view(request):
    user_devices = DeviceList.objects.filter(user=request.user)
    total_estimated_price = user_devices.aggregate(total=Sum('device__estimated_price'))['total'] or 0
    return render(request, 'cashify_app/device_list.html', {
        'user_devices': user_devices,
        'total_estimated_price': total_estimated_price,
        'has_devices' : user_devices
    })

@login_required
def device_create_view(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'cashify_app/device_form.html', {'form': form})


@login_required
def add_to_list(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if device.status.lower() == 'unavailable':
        messages.error(request, 'This device is unavailable')
        return redirect('home')
    DeviceList.objects.get_or_create(user=request.user, device=device)
    return redirect('device_detail', device_id=device.id)


@login_required
def remove_from_list(request, device_id):
    device_list_item = get_object_or_404(DeviceList, user=request.user, device_id=device_id)
    device_list_item.delete()
    return redirect('device_list')

@login_required
def device_detail_view(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    return render(request, 'cashify_app/device_detail.html', {'device': device})

@login_required
def transaction_view(request):
    transactions = Transaction.objects.filter(user=request.user)
    has_transactions = transactions.exists()
    return render(request, 'cashify_app/transactions.html', {
        'transactions': transactions,
        'has_transactions': has_transactions
    })

@login_required
def make_payment_view(request):
    # Placeholder for payment logic
    return HttpResponse("Payment process coming soon.")
