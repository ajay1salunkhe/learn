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
                for i in l2:
                    for j in i:
                        print("j = ",j)
                        l2[cr][cc] = int(j) - int(minr[cr])
                        cc=cc+1
                    cr=cr+1
                    cc=0
                
                minc=[]
                l2 =  list(map(list, zip(*l2)))
                for i in l2:
                    minc.append(min(i))
                cr=0
                cc=0
                print("l1 = ",l1)
                print("l2 = ",l2)
                print("minc = ",minc)
                l3=deepcopy(l2)
                for i in l2:
                    for j in i:
                        print("j= ",j)
                        l3[cr][cc] = int(j) - int(minc[cr])
                        cc=cc+1
                    cr=cr+1
                    cc=0
                print("minc = ",minc)                    
                l2 =  list(map(list, zip(*l2)))
                l3 =  list(map(list, zip(*l3)))

                countzero = 0 
                for i in l3:
                    for j in i:
                        if j==0:
                            countzero = countzero + 1
                    if countzero==1:
                         for j in range(len(i)):
                            if i[j]==0:
                                i[j]='0'    
                    countzero=0

                print("l3 = ",l3)    

                file1=""
                '''
                from django.core.files.storage import FileSystemStorage
                from django.http import HttpResponse
                from django.template.loader import render_to_string

                from weasyprint import HTML
                print("hgjhgsjfgsdf  jsgsgjh gfsdfg jhg  ksdf g")
                
                html_string = render_to_string('opt_tech/ass_problem_ans.html', {"l1":list(l1),"l2":list(l2),"l3":list(l3),"minr":list(minr),"minc":list(minc),"rows":range(1,rows+1),"cols":range(1,cols+1)})  
                
                html = HTML(string=html_string)
                html.write_pdf(target='/tmp/mypdf.pdf');
                file1=""
                fs = FileSystemStorage('/tmp')
                with fs.open('mypdf.pdf') as pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
                    return response
                    file1=response
                '''
                return render(request, 'opt_tech/ass_problem_ans.html', {"l1":list(l1),"l2":list(l2),"l3":list(l3),"minr":list(minr),"minc":list(minc),"rows":range(1,rows+1),"cols":range(1,cols+1),"file1":file1})  
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
