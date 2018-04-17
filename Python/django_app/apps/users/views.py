# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *

# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request) :

    return render(request, 'users/new.html')

def create(request) :
    # form = ContactForm(request.Post)
    # print request.POST['name']
    user = User(name = request.POST['name'], email = request.POST['email'])
    # print user
    user.save()
    # print User.objects.all()
    return redirect('/users')

def show(request, id) :
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'users/show.html'.format(id), context)

def edit(request, id) :
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'users/edit.html'.format(id), context)

def update(request, id) :
    user = User.objects.get(id=id)
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.save()
    return redirect(reverse('index'))

def destroy(request, id) :
    
    User.objects.get(id=id).delete()
    return redirect('/users')

    