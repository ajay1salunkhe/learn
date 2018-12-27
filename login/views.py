from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from tutorial.views import home

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "Signed Up Successfully. Login Here")
            return redirect('home')
        else:
            for f in form:
                messages.error(request, f.errors)
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})
