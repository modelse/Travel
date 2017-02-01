from __future__ import unicode_literals
from ..Log.models import User
from django.db import models
from datetime import datetime
import time
from dateutil.parser import parse as parse_date

class TripManager(models.Manager):

    def validation(self,request):
        errors=[]
        if len (request.POST['destination'])<2:
            errors.append('Please enter a destination.')
        if len(request.POST['description'])<5:
            errors.append('Please enter a trip description.')
        if len(request.POST['toDate'])<6:
            errors.append('Please enter a Travel Date To date.')
        if len(request.POST['fromDate'])<6:
            errors.append('Please enter a Travel Date From date.')
        if (request.POST['fromDate']):
            date=datetime.strptime(request.POST['fromDate']+ " "+ "00:00", "%Y-%m-%d %H:%M")
            if not datetime.now()<  date:
                errors.append('Date must be in the future.')
        if (request.POST['toDate']):
            date=datetime.strptime(request.POST['fromDate']+ " "+ "00:00", "%Y-%m-%d %H:%M")
            future=datetime.strptime(request.POST['toDate']+ " "+ "00:00", "%Y-%m-%d %H:%M")
            if future<date:
                errors.append('To Date must be after from Date')
        return errors



    def AddTrip(self,request):
        Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], travelFrom=request.POST['fromDate'], travelTo=request.POST['toDate'], user=User.objects.get(id=request.session['user_id']))

class ListManager(models.Manager):
    def AddExisting(self,request):
        TripList.objects.create(trip=Trip.objects.get(id=request.session['tripid']), user=User.objects.get(id=request.session['user_id']))

    def Join(self, request):
        TripList.objects.create(trip=Trip.objects.get(id=request.session['trip']), user=User.objects.get(id=request.session['user_id']))


class Trip(models.Model):
    destination=models.CharField(max_length=150)
    description=models.CharField(max_length=300)
    travelFrom=models.CharField(max_length=10)
    travelTo=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User)
    objects=TripManager()

class TripList(models.Model):
    user=models.ForeignKey(User)
    trip=models.ForeignKey(Trip)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ListManager()
