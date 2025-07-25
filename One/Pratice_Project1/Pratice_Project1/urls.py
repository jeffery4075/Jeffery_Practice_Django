"""
URL configuration for Pratice_Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter',views.First_Function),
    path('string_filter',views.String_Only_Filter),
    path('date',views.date_time),
    path('if_condi',views.if_condition),
    path('for_loop',views.for_loop1),
    path('for_loop2',views.learn_django),
    path('student_view', views.student_view),
    path('simple_get1',views.simple_get1),
    path('main_post1',views.main_post1),
    path('temp_converter',views.temp_converter),
    path('currency_result', views.currency_result, name='currency_result'),
    path('currency_converter',views.currency_converter,name='currency_converter'),
    path('calcu_output',views.calcu_output,name='calcu_output'),
    path('',views.calcu_main,name='calcu_main'),
]
