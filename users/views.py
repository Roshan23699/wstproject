from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from shop.models import Product
from users.models import Cart, Wishlist, Orders, Profile
from django.http import HttpResponseRedirect
import smtplib
from email.message import EmailMessage


def register(request):
    carx = None
    if request.user.is_authenticated:
	    carx = len(Cart.objects.filter(user=request.user))
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created. Log In to continue')
            return redirect('login')
    else:
        forms = UserRegisterForm()
    return render(request, 'users/register.html', {'form': forms, 'cart': carx})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form, 
        'cart': len(Cart.objects.filter(user=request.user))
    }
    return render(request, 'users/profile.html', context)


