from django.shortcuts import render

def	home(request):
    return render(request,	'tutorial/home.html',	{})
