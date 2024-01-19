from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from musicians.forms import musicians_form
from musicians.models import musician_Model

# Create your views here.
def add_musician(request):
    if request.method == "POST":
        Musician_form = musicians_form(request.POST)
        if Musician_form.is_valid():
            print(Musician_form.cleaned_data)
            Musician_form.save()
            redirect("add_musician")
    else: 
        Musician_form = musicians_form()
    return render(request,"add_musician.html",{'Musician_form':Musician_form})

def edit_musician(request,id):
    musician = musician_Model.objects.get(pk=id)
    Musician_form = musicians_form(instance=musician)

    if request.method == "POST":
        Musician_form = musicians_form(request.POST)
        if Musician_form.is_valid():
            Musician_form.save()
            return redirect("add_musician")
   
    return render(request,"add_musician.html",{'Musician_form':Musician_form})


def delete_musician(request,id):
    Musician = musician_Model.objects.get(pk=id)
    Musician.delete()
    return redirect('homepage')
    

