from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

def home(request, year, month):
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

    cal = cal[0].replace('\n', '')


    return render( request, 'home.html', {
        'user':user, 
        'year':year, 
        'month': month,
        'month_num':month_num,
        'cal': cal,
        
        
        })
