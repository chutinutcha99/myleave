from django import forms
from django.forms import ModelForm, widgets
from .models import Profile, Department_Setting, Member, Leave_Form, SORT_NAME, DEPARTMENT_NAME, DURATION1, DURATION2


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            "firstname",
            "lastname",
            "email",
            "password",
            "repassword",
            "gender",
            "mobile",
        ]

class Department_Setting_Form(forms.ModelForm):

    class Meta:

        model = Department_Setting

        fields = [
            "department_name"
        ]

class MemberForm(forms.ModelForm):

    class Meta:

        model = Member

        fields = [
            "member_type"
        ]

class DateInput(forms.DateInput):
    input_type = "date"

class LeaveForm(forms.ModelForm):
    leave_sort_name = forms.ChoiceField(choices=SORT_NAME, widget=forms.Select, initial='--')
    leave_reason = forms.CharField(widget=forms.Textarea)
    '''start_date = forms.DateField(widget=DateInput(format='%Y/%m/%d'), input_formats=('%Y/%m/%d',))'''
    start_date = forms.DateField()
    duration1 = forms.ChoiceField(choices=DURATION1, widget=forms.Select, initial='--')
    '''end_date = forms.DateField(widget=DateInput(format='%Y/%m/%d'), input_formats=('%Y/%m/%d',))'''
    end_date = forms.DateField()
    duration2 = forms.ChoiceField(choices=DURATION2, widget=forms.Select, initial='--')
    leave_contact = forms.CharField(widget=forms.Textarea)

    class Meta: 

        model = Leave_Form

        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 
                        'placeholder': 'Select a date',
                        'type': 'date'
                        }),
        }



