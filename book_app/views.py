from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views import generic
from django.urls import reverse_lazy
import os

# Create your views here.



class authregisterclass(generic.CreateView):
    form_class = authregform
    template_name = 'registeration.html'
    success_url = reverse_lazy('index')


class index(generic.View):
    form_class = logform
    template_name = 'index.html'
    def get(self,request):
        form= self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        if request.method=='POST':
            a=logform(request.POST)
            if a.is_valid():
                em= a.cleaned_data['email']
                ps= a.cleaned_data['password']
                b=User.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return redirect(f'http://127.0.0.1:8000/book_app/profile/{i.id}')
                else:
                    return HttpResponse("Login Failed")


class profile(generic.CreateView):
    form_class = bookform
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    model = addbook
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        a1=User.objects.get(id=id)
        a=addbook.objects.all()
        id1=[]
        bknm=[]
        authname=[]
        bkpdf=[]
        bkimg=[]
        dat=[]
        for i in a:
            id=i.id
            id1.append(id)
            bn=i.boname
            bknm.append(bn)
            an=i.auname
            authname.append(an)
            bp=str(i.bopdf).split('/')[-1]
            bkpdf.append(bp)
            bi=str(i.boimage).split('/')[-1]
            bkimg.append(bi)
            dt=i.date
            dat.append(dt)
        mylist= zip(id1,bknm,authname,bkpdf,bkimg,dat)
        return render(request,self.template_name,{'a':mylist,'a1':a1})



class bookdelete(generic.DetailView):
    model = addbook
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')












