from django.shortcuts import render,redirect
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

def simple_get1(request):

    val1 = int(request.POST.get('First_number',0))
    val2 = int(request.POST.get('Second_number',0))
    
    res = val1 + val2
    return render(request,'Get_method1.html',{'sum':res})

def main_post1(request):
    if request.method == "POST":
        raw1 = request.POST.get('first_number',0)
        raw2 = request.POST.get('second_number',0)
        try:
            val1 = int(raw1)
            val2 = int(raw2)
            sum = val1 +val2
            data = {
                'da1' : val1,
                'da2' : val2,
                'da_sum' : sum
            }
        except ValueError:
            sum = "Enter valid integers."
        return render(request,'Post_method1.html',data)
    else:
        return render(request,'Post_method1.html')

def temp_converter(request):
    if request.method == "POST":
        raw1 = request.POST.get('first_temp',0)
        temp = {}
        try:
            Celsius = float(raw1)
            Fahrenheit = Celsius * 9 / 5 + 32
            temp = {
                'Ce': Celsius,
                'Fa': Fahrenheit
            }
        except ValueError:
            temp = {
                'error': "Enter a valid temp"
            }
        return render(request, 'Temperature_Converter.html', temp)
    else:
        return render(request, 'Temperature_Converter.html')
