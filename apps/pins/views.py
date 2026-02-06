from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pin
from .forms import PinForm

def pin_detail(request, pin_id):
    pin = get_object_or_404(Pin, id=pin_id)
    return render(request, 'pins/pin_detail.html', {'pin': pin})

@login_required
def pin_create(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            return redirect('pins:pin_detail', pin_id=pin.id)
    else:
        form = PinForm(user=request.user)
    return render(request, 'pins/pin_form.html', {'form': form})
