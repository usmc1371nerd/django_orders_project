from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime   import datetime
import pytz 

def home(request, year= datetime.now().year, month=datetime.now().strftime('%B')):
    user = "JP"
    month = month.title()
    #convert month from name to number
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    # create calendar 
    cal = HTMLCalendar().formatmonth(
        year,
        month_num,
        
    ).replace('\n', ''), 

    #get current year
    now = datetime.now()
    current_year= now.year 

    #get current time
    your_timezone = pytz.timezone('America/Chicago')
    time = now.astimezone(your_timezone).strftime('%I:%M %p')

    cal = cal[0].replace('\n', '')


    return render( request, 
        'orders/home.html', {
        'user':user, 
        'year':year, 
        'month': month,
        'month_num':month_num,
        'cal': cal,
        'current_year': current_year,
        'time' : time
        
        
        })
