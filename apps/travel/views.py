from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages

from .models import Users, Trip
from django.db.models import Count
import bcrypt

def index(request):

    return render(request, "travel/index.html")

# Create your views here.
def register(request):

    regCheck = Users.objects.register(request.POST)

    if regCheck['success']:
        messages.success(request, "Succesful Registrations")
        request.session['user_id'] = regCheck['user_id']
        user = Users.objects.get(id = regCheck['user_id'])

        return redirect('/')
    else:
        for error in regCheck['errors']:
            messages.error(request, error)
        return redirect('/')

def login(request):

    logCheck = Users.objects.login(request.POST)
    if logCheck['success']:
        request.session['user_id'] = logCheck['user_id']


        return redirect('/travels')
    else:
        for error in logCheck['errors']:
            messages.error(request, error)
        return redirect('/')


def travels(request):



    context = {

    'user' : Users.objects.get(id = request.session['user_id']),
    'trips' : Trip.objects.all()

    }
    return render(request, "travel/travels.html", context)

def add(request):
    thisUser = Users.objects.get(id = request.session['user_id'])
    return render(request, 'travel/add_trip.html')



def addTrip(request):

    travel_form = {

    'destination' : request.POST['destination'],
    'description' : request.POST['description'],
    'start_date' : request.POST['date_from'],
    'end_date' : request.POST['date_to'],
    'user_id' : request.session['user_id'],

    }

    quoteCheck = Trip.objects.quoteReg(travel_form)

    if quoteCheck['success']:

        return redirect('/travels')
    else:
        for error in quoteCheck['errors']:
            messages.error(request, error)
        return redirect('/add')

def logout(request):
    request.session.pop('user_id')
    messages.success(request, "You are logged out")
    return redirect('/')

def join(request, id):
    thisuser = Users.objects.get(id = request.session['user_id'])
    trip = Trip.objects.get(id = id)
    trip.join.add(thisuser)
    return redirect('/travels')

def destination(request, id):
    thisuser = Users.objects.get(id = request.session['user_id'])
    trip = Trip.objects.get(id = id)
    context = {

    'user': thisuser,
    'trips': trip

    }
    return render(request, "travel/destination.html", context)
