from django.shortcuts import render
from django.shortcuts import HttpResponse

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
