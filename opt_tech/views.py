from django.shortcuts import render, redirect

def problems(request):
    return render(request, 'opt_tech/problems.html', {})