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

def for_loop1(request):
    student = {'names': ['Jeffery', 'John', 'Smith', 'Kumar', 'Ravi', 'Luke', 'Riya', 'Emily', 'Sophia', 'Michael', 'David', 'Olivia'],}
    return render(request,'For_Loop.html',context=student)

def learn_django(req):
    stu = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Sonam', 'roll': 102},
        'stu3': {'name': 'Raj', 'roll': 103},
        'stu4': {'name': 'Anu', 'roll': 104},
    }
    students = {'student': stu}
    return render(req, 'For_Loop2.html', context=students)


def student_view(request):
    students = {
        'stu1': {'name': 'Rahul', 'roll': 101, 'marks': 85, 'subjects': ['Math', 'Science', 'English']},
        'stu2': {'name': 'Sonam', 'roll': 102, 'marks': 90, 'subjects': ['History', 'Math']},
        'stu3': {'name': 'Raj', 'roll': 103, 'marks': 78, 'subjects': ['English', 'Science', 'Math']},
        'stu4': {'name': 'Anu', 'roll': 104, 'marks': 92, 'subjects': ['Math', 'English']},
    }
    return render(request, 'For_Loop_Questions1.html', context={'students': students})

