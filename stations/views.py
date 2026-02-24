from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Station

def public_home(request):
    stations = Station.objects.all()
    return render(request, "stations/public.html", {"stations": stations})

@login_required
def staff_dashboard(request):
    stations = Station.objects.all()
    return render(request, "stations/staff.html", {"stations": stations})