from django.shortcuts import render, redirect
from .forms import RowColForm
from django.contrib import messages

errorr = ""
def problems(request):
    return render(request, 'opt_tech/problems.html', {})

def ass_problem(request):
    if request.method == 'POST':
        print("request.POST.get = ",request.POST.get('11'))
        form = RowColForm(request.POST)
        print("form data = ",form.data)
        l1=[]
        l2=[]
        l3=[]
        try:   
            if str(request.POST.get('flag'))=="True":
                l1=[]
                temp=[]
                cols=int(request.POST.get('ncols'))
                rows=int(request.POST.get('nrows'))
                for i in range(1,rows+1):
                    for j in range(1,cols+1):
                        temp.append(int(request.POST.get(str(i)+str(j))))
                    l1.append(temp)
                    temp=[]

                print("l1 = ",l1)
                from copy import deepcopy
                l2=deepcopy(l1)
                minr=[]
                for i in l1:
                    minr.append(min(i))
                cr=0
                cc=0
                print("minr = ",minr)
                for i in l2:
                    for j in i:
                        print("j = ",j)
                        l2[cr][cc] = int(j) - int(minr[cr])
                        cc=cc+1
                    cr=cr+1
                    cc=0
                
                print("l2 = ",l2)
                print("l1 = ",l1)
                minc=[]
                '''
                import numpy as np
                minc=np.min(l2, axis=0)
                l3 = list(l2-minc)
                minc  = list(minc) '''
                return render(request, 'opt_tech/ass_problem_ans.html', {"l1":list(l1),"l2":list(l2),"l3":list(l3),"minr":list(minr),"minc":list(minc),"rows":range(1,rows+1),"cols":range(1,cols+1)})  
        except Exception as e:
            print(str(e))
            messages.error(request, "Errorr = ",str(e)+str(l1)+str(l2)+str(l3))            
            
        if form.is_valid():
            rows = form.cleaned_data.get('rows')
            cols = form.cleaned_data.get('cols')
            
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
