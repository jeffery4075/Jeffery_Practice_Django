from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.

def First_Function(request):

    name = 'Jeffery'
    age = '25'
    Phone_Number = '974864908'
    content={'Name':name,'Age':age,'Phone_Number':Phone_Number}
    return render(request,'First_Template.html',content)

def String_Only_Filter(request):
    context = {
    'username':    'jane_doe42',
    'tagline':     '',
    'description': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.',
    'headline':    'welcome_to my blog!'
    }
    return render(request, 'string_filter.html', context)

def date_time(request):
    da = datetime.now()
    return render(request, 'dateAndTime.html', {'date': da})

def if_condition(request):
    content = {
        'sn' : True,
        'mn' : True,
        'val1':'django',
        'val2':'Jeffery'
    }
    return render(request,'if_condition.html',content)