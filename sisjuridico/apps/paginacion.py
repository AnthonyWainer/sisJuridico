#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def paginacion(request,tab,modulo,url):
    if request.GET.get('pag'):
        pag=request.GET.get('pag')
        pag=int(pag)
    else:
        pag=10
    paginator = Paginator(tab,pag)
    page = 1
    if request.is_ajax():  
        query = request.GET.get('page')
        if query is not None:
            page = query
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)

    r = lista.paginator.num_pages
    p = 1
    if r >=30:
        p = 1
        r = 30

    if int(page)>30:
        s= 30*((int(page)-1)/30)
        p += s
        r += s

    nroP = (int(page)-1)*pag
    modulo.update({'lista':lista,'range':range(p,r+1),'nroP':nroP,'pag':pag})

    return render(request,url,modulo)