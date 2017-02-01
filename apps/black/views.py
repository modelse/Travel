from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..Log.models import User
from .models import Trip,TripList
from django.contrib import messages
import datetime

def index(request):
    return render(request, 'Log/index.html')
def home(request):
    context={
    "trip":TripList.objects.filter(user=request.session['user_id']),
    "otherTrip":TripList.objects.exclude(user=request.session['user_id'])
    }
    return render(request, 'black/home.html', context)
def addTrip(request):
    return render(request, 'black/create.html')
def create(request):

    errors = Trip.objects.validation(request)

    if not errors == []:
        for error in errors:
            messages.info(request, error)
        return redirect('/addTrip')
    else:
        Trip.objects.AddTrip(request)
        request.session['createdBy']=request.session['user_id']

        request.session['tripid']=Trip.objects.only('id').get(destination=request.POST['destination']).id


    return redirect(reverse('blackApp:addtoList'))

def addtoList(request):
    TripList.objects.AddExisting(request)
    return redirect(reverse('blackApp:home'))

def add(request, id):
    request.session['trip']=Trip.objects.only('id').get(id=id).id
    TripList.objects.Join(request)
    return redirect(reverse('blackApp:home'))

def view(request, id):
    context={
    'trip':Trip.objects.filter(id=id),
    'other':TripList.objects.filter(trip=id)
    }
    return render(request, 'black/view.html', context)

def logout(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
	return redirect(reverse('loginApp:index'))
