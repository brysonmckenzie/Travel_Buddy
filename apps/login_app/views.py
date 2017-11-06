# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from datetime import datetime

from django.core.urlresolvers import reverse

from ..travel_app.models import User

# import bcrypt4

def login(request):
    
    return render(request,'login_app/login.html')


def register(request):
    

    
    return render(request,'login_app/register.html')





def register_process(request):
    
    server_firstname = request.POST['html_firstname']
    server_lastname = request.POST['html_lastname']
    server_username = request.POST['html_username']
    server_password = request.POST['html_password']

    isValid = True 

    if (len(request.POST['html_firstname']) <= 1):
        messages.error(request,'Invalid field length for first name!')
        isValid = False

    if (request.POST['html_firstname'].isalpha() == False):
        messages.error(request,'Invalid field length for first name!')
        isValid = False

    if (len(request.POST['html_lastname']) < 3):
        messages.error(request,'Invalid field length for last name!')
        isValid = False

    if (request.POST['html_lastname'].isalpha() == False):
        messages.error(request,'Invalid field length for first name!')
        isValid = False

    if (len(request.POST['html_username']) < 3):
        messages.error(request,'Invalid field length for user name!')
        isValid = False

    if (len(request.POST['html_password']) != request.POST['html_passconf']):
        messages.error(request, 'Passwords doesnt match')

        if not isValid:

            return redirect(reverse("user:register"))    

    
        
    User.objects.create(
        first_name = server_firstname,
        last_name = server_lastname,
        user_name = server_username,
        password = server_password,
    )
    print '****************New User*********************'

    return redirect('/')


def login_process(request):
    
    server_username = request.POST['html_username']
    server_password = request.POST['html_password']
    user = User.objects.get(user_name = server_username)
    
    if request.method == 'POST':
        
        server_username = request.POST['html_username']
        server_password = request.POST['html_password']
       

    
        if len(request.POST['html_username']) < 3:
            
            # try: 
                
            
            
            # except:

                # messages.error(request, 'Invalid field length for user name!')

                return redirect('/login')

        elif len(server_password) < 1:
            
            # messages.error(request, 'Enter a password!')

            return redirect('/login')

        else:
            
            user = User.objects.get(user_name = server_username)
            if server_password == user.password:
                
                request.session['user_id'] = user.id
                print "********** User Logged IN**************"
                print "**** User ID = "+ str(user.id) + " *** ID IN SESSIONS ***" 
                print "The user #" + str(user.id) + "has now logged in the system" + str(datetime.now())
                print "***************************************"
                return redirect('/')

def log_out(request):
    
    request.session.clear()

    return redirect('/login')



