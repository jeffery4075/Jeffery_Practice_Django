from django.shortcuts import render
from app.models import Profile


def pro(request):
    stu = Profile.objects.all()
    print(stu)
    return render(request,'Profile.html')
