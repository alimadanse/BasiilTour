from django.views import generic
from django.urls import reverse_lazy
from .forms import CusomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'home.html', {'error': 'Invalid username or password'})

    return render(request, 'home.html')


class SignUpView(generic.CreateView):
    form_class = CusomUserCreationForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')
    
