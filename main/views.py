from django.shortcuts import render, redirect
from .forms import TourRegisterForm
from .models import TourRegistration

def reserve_form(request):
    if request.method == 'POST':
        form = TourRegisterForm(request.POST)
        if form.is_valid():
            registration = TourRegistration()
            
            registration.first_name = form.cleaned_data['first_name']
            registration.last_name = form.cleaned_data['last_name']
            registration.nat_id = form.cleaned_data['nat_id']
            registration.age = form.cleaned_data['age']
            registration.phone_number = form.cleaned_data['phone_number']
            
            registration.save()  
            
            return redirect('reserve_form')  
    else:
        form = TourRegisterForm()
    return render(request, 'home.html', {'form': form})


def home(request):
    return render(request, 'home.html')