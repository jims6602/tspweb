from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from .models import Event

def index(request):

        if(0 == 1):

            e1 = Event(name='SALARY INCREASE', description='salary increase by 2.5',  status='I')
            e1.save()

            e2 = Event(name='MARRIAGE', description='Payout adjustment',  status='I')
            e2.save()

            e3 = Event(name='SALARY INCREASE', description='salary increase by 1.5',  status='I')
            e3.save()

            e4 = Event(name='SALARY INCREASE', description='salary increase by 0.5',  status='I')
            e4.save()

            e5 = Event(name='SALARY INCREASE', description='salary increase by 2.8',  status='I')
            e5.save()

            e6 = Event(name='SALARY INCREASE', description='salary increase by 2.9',  status='I')
            e6.save()

        return render(
        request,
        'Events/index.html',
        {
            'title':'Events',
            'year':datetime.now().year,
            'Events': Event.objects.all()
        }
    )
