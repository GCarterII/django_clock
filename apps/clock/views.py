from django.shortcuts import render, redirect, render
import datetime

def clock(request):

    current_date_time = datetime.datetime.now()
    context = {
        'month': current_date_time.strftime('%b'),
        'day': current_date_time.day,
        'year': current_date_time.year,
        'time':current_date_time.strftime('%I:%M %p')
    }
    return render(request, "clock/index.html", context)


# Create your views here.
