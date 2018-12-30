from django.shortcuts import render

def	home(request):
    return render(request,	'tutorial/home.html',	{})

def aboutus(request):
    return render(request,	'aboutus/aboutus.html',	{})

def categories(request):
    return render(request,	'tutorial/categories.html',	{})

def tutorials(request):
    return render(request,	'tutorial/tutorials.html',	{})
