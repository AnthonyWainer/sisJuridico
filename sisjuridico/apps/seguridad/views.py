from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Crea tus vista aqui.
def index(request):
	return render_to_response('seguridad/index.html')

