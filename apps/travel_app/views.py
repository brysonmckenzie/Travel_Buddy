# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import *

from django.contrib import messages

# Get Route functions

def index(request):
    

    context = {
        'current_user': User.objects.get(id = request.session['user_id']),
        'trips': Trip.objects.all(),
        'my_trips': Trip.objects.filter(users_id = request.session['user_id']),
        }
        
    

    return render(request,'travel_app/index.html', context)


def destination(request, id):
  
        
    context = {
        'trips': Trip.objects.get(id = id),
        'peeps': Trip.objects.all(),
        }
       

    

    return render(request,'travel_app/destination.html', context)




def add_trip(request):

    return render(request,'travel_app/add_trip.html')

    #POST Route functions

def add_trip_process(request):
    
    current_user = request.session['user_id']
    server_destination = request.POST['destination']
    server_description = request.POST['description'] 
    server_start_date = request.POST['start_date'] 
    server_end_date = request.POST['end_date'] 
    

    if request.method == 'POST':
        
        trip = Trip.objects.create(destination = server_destination, description = server_description, start_date = server_start_date, end_date = server_end_date, users_id = current_user, join = "true"),

        print '*********** Trip Added ********** by USER ID' + str(current_user)
        print '************************************************'
    return redirect('/')

def join(request, id):
    
    # if "current_user" not in request.session:
    #     messages.error(request, "Please login")
    #     return redirect('/')

    
    u = Trip.objects.get(id = id)
    print u.destination
    if request.method == 'POST':
        
        
        u.join = "true"
        u.save()
        
        print "****************"
        print "*** Going on Trip ***"
        print "****************"

    return redirect('/')

def not_join(request, id):
    
    # if "current_user" not in request.session:
    #     messages.error(request, "Please login")
    #     return redirect('/')

    
    u = Trip.objects.get(id = id)
    print u.destination
    if request.method == 'POST':
        
        
        u.join = ""
        u.save()
        
        print "****************"
        print "*** Going on Trip ***"
        print "****************"

    return redirect('/')



def log_out(request):
    
    if request.method == 'POST':
        request.session.clear()

    return redirect('/login')
