from django.shortcuts import render

def	home(request):
    return render(request,	'tutorial/home.html',	{})

def	tryresponse(request):
    return render(request,	'response.xml',	{})

def aboutus(request):
    return render(request,	'aboutus/aboutus.html',	{})

def categories(request):
    return render(request,	'tutorial/categories.html',	{})

def tutorials(request):
    return render(request,	'tutorial/tutorials.html',	{})

def content(request):
    return render(request,	'tutorial/content.html',	{})