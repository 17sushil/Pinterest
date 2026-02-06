from django.shortcuts import render
from apps.pins.models import Pin


def home(request):
    """Home page view with search"""
    query = request.GET.get('q')
    if query:
        pins = Pin.objects.filter(title__icontains=query) | Pin.objects.filter(description__icontains=query)
    else:
        pins = Pin.objects.all().order_by('-created_at')
    
    return render(request, 'base/home.html', {'pins': pins, 'query': query})


def explore(request):
    """Explore page view"""
    pins = Pin.objects.all().order_by('?')
    return render(request, 'base/explore.html', {'pins': pins})
