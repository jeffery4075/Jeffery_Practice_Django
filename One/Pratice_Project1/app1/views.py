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


def currency_result(request):
    # Get values from the session
    amount_sar = request.session.get('amount_sar')
    amount_inr = request.session.get('amount_inr')
    return render(request, 'currency_result.html', {'amount_sar': amount_sar, 'amount_inr': amount_inr})

    
def currency_converter(request):
    if request.method == "POST":
        raw1 = request.POST.get('amount',0)

        try:
            exchange_rate = 23
            amount_in_sar  = float(raw1)
            amount_in_inr = amount_in_sar * exchange_rate

            # Store the result in session
            request.session['amount_sar'] = amount_in_sar
            request.session['amount_inr'] = amount_in_inr

            return redirect('currency_result')
        except ValueError:
            content ={
                'Error_key':'Enter a valid input',
            }
            return render(request,'Currency_conversion.html',content)
    else:
        return render(request,'Currency_conversion.html')
    

def calcu_output(request):
    recived_res = request.session.get('tarnsfer_result')
    recived_num1 = request.session.get('tarnsfer_num1')
    recived_num2 = request.session.get('tarnsfer_num2')
    recived_oper = request.session.get('tarnsfer_oper')
    recived_error = request.session.get('tarnsfer_error')

    return render(request,'Calculator_Output.html',{'recived_res':recived_res,'recived_num1':recived_num1,
                                                   'recived_num2':recived_num2,'recived_oper':recived_oper,
                                                   'recived_error':recived_error})

def calcu_main(request):
    if request.method == "POST":
        raw1 = request.POST.get('first_number',0)
        raw2 = request.POST.get('second_number',0)

        result = None
        error = None

        try:
            num1 = float(raw1)
            num2 = float(raw2)
            oper = request.POST.get('operation',None)

            if oper == "Add":
                result = num1 + num2
            elif oper == "Subtract":
                result = num1 - num2
            elif oper == "Multiply":
                result = num1 * num2
            elif oper == "Divide":
                if num2 == 0:
                    error = "Error: Cannot divide by zero!"
                else:
                    result = num1 / num2
            else:
                error = "Invalid operation selected."

            request.session['tarnsfer_result'] = result
            request.session['tarnsfer_num1'] = num1
            request.session['tarnsfer_num2'] = num2
            request.session['tarnsfer_oper'] = oper
            request.session['tarnsfer_error'] = error

            return redirect('calcu_output')
        except ValueError:
            error_msg={'error_key':'Enter a valid input'}
            return render(request,'Calculator_main.html',error_msg)
    
    else:
        return render(request,'Calculator_main.html')
