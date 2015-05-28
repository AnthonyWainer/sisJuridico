from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import formCategoria

# Crea tus vista aqui.
@login_required(login_url='/')
def registro_expediente(request):
    return render_to_response('expediente/registro_expediente.html',{'mod':'mod'})    

@login_required(login_url='/')
def registro_categoria(request):
    formu = formCategoria()
    return render_to_response('expediente/registro_categoria.html',{'form': formu}) 
