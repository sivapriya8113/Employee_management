from django.shortcuts import render, redirect
from .forms import EmployeeForm,NumWordForm
from .models import Employee
from django.shortcuts import  render, redirect
from num2words import num2words
from gtts import gTTS
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import gtts
from playsound import playsound
import os
import pyttsx3

# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)

        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            print("@@@@@@@@@@@@@@",form)
            form.save()
            print("1234567876542345678",form)
        return redirect('/Admin/')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    print("asdfgh")
    return redirect('/Admin/')

def num_to_word(request):
    forms = NumWordForm(request.POST or None)
    print(request.POST)
    word = 'Please enter your number'
    if forms.is_valid():
        number = forms.cleaned_data.get('Number')
        print(number)
        word = num2words(number, to='cardinal')
        print(word)
    else:
        print("else")
    tts = gtts.gTTS(word)
    tts.save("Speech.mp3")
    #playsound("Speech.mp3",False)
    context = {"form": forms, "word": word}
    return render(request, 'employee_register/num_to_word.html', context=context)

