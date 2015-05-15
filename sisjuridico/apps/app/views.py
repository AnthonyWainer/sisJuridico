from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime

# Crea tus vista aqui.
def index(request):
	return render_to_response('app/index.html')


def hora_actual(request):
    now = datetime.now()
    return render_to_response('app/hora.html',{'hora':now})