from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()           
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been successfully created. You can now login.')
            return redirect('home')
    else:
        form = UserRegisterationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)



class HomeListView(ListView):
    model = User
    template_name = 'user/home.html'



class EventListView(ListView):
    model = User
    template_name = 'user/events.html'


class ProfileView(ListView):
    model = User
    template_name = 'user/profile.html'