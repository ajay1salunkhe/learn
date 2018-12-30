from django.shortcuts import render

def	home(request):
    return render(request,	'tutorial/home.html',	{})

def aboutus(request):
    return render(request,	'aboutus/aboutus.html',	{})

def tutorials(request):
    return render(request,	'tutorial/tutorials.html',	{})
