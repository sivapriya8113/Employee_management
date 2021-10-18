from django import forms
from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('EMPimage','fullname','mobile','emp_code','Email','Password','Address')
        labels = {
            'EMPimage':' EMPimage',
            'fullname':'Full Name',
            'emp_code':'EMP. Code',
            'mobile':'Mobile Number',
            'Email':'Email',
            'Password':'Password',
            'Address':'Address'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        #self.fields['Department'].empty_label = "Select"
        self.fields['emp_code'].required = False





