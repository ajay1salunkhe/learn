from django.shortcuts import render, redirect
from .forms import RowColForm
from django.contrib import messages

def problems(request):
    return render(request, 'opt_tech/problems.html', {})

def ass_problem(request):
    if request.method == 'POST':
        print("request.POST.get = ",request.POST.get('11'))
        form = RowColForm(request.POST)
        print("form data = ",form.data)
        try:   
            if str(request.POST.get('flag'))=="True":
                for i in range(1,int(request.POST.get('nrows'))):
                    for j in range(1,int(request.POST.get('ncols'))):
                        print("value = ",request.POST.get(str(i)+str(j)))
                return render(request, 'opt_tech/ass_problem_ans.html', {})  
        except:
            pass
        if form.is_valid():
            rows = form.cleaned_data.get('rows')
            cols = form.cleaned_data.get('cols')
            print("roww = ",rows,"  ",type(rows))
            print("colss = ",cols,"  ",type(cols))
            
            if(rows>0 and cols>0):
                return render(request, 'opt_tech/ass_problem_next.html', {'rows':range(1,rows+1),'cols':range(1,cols+1),'nrows':rows, 'ncols':cols, 'flag':"True"})  
            else:
                messages.error(request, "Invalid no of row/column, Value should be positive integer")            
        else:
            pass
    else:
        form = RowColForm()
    return render(request, 'opt_tech/ass_problem.html', {'form':form})


def ass_problem_ans(request):
    if request.method == 'POST':
        print("request.POST = ",request.POST)
    else:
        pass
    return render(request, 'opt_tech/ass_problem_ans.html', {})
