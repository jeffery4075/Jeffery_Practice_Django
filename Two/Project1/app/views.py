from django.shortcuts import render
from app.models import Profile


# def pro(request):
#     stu = Profile.objects.all()
#     print(stu)
#     return render(request,'Profile.html',{'data':stu})

from django.shortcuts import render, redirect
from app.models import Profile

def pro(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        email = request.POST.get('email')
        city  = request.POST.get('city')
        # create and save a new Profile
        Profile.objects.create(Name=name, Email=email, city=city)
        # redirect to the same page to clear POST data
        return redirect('profile')

    # GET (or after redirect): show pipall profiles
    students = Profile.objects.all()
    return render(request, 'Profile.html', {'data': students})

