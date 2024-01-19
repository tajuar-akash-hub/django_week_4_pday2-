from django.shortcuts import render,redirect
from django.http import HttpResponse
from albums.forms import album_form
from . import forms
from albums.models import albums_Model

# Create your views here.
def add_album(request):
    if request.method == "POST":
        Album_form = album_form(request.POST)
        if Album_form.is_valid():
            Album_form.save()
            redirect("add_album")
    else : 
        Album_form = album_form()

    return render(request,"add_album.html",{'Album_form':Album_form})

def edit_album(request,id):
    Album = albums_Model.objects.get(pk=id)
    Album_form = album_form(instance=Album)

    if request.method == "POST":
        Album_form = album_form(request.POST,instance=Album)
        if Album_form.is_valid():
            Album_form.save()
            return redirect('homepage')
    return render(request,"add_album.html",{'Album_form':Album_form})



