from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, MonthPickerInput, YearPickerInput


class MyDatePickerInput(DatePickerInput):
    template_name = 'orders/order/date-picker.html'


class OrderCreateForm(forms.ModelForm):
    agree_term = forms.BooleanField(required=True, help_text="I accept the terms and conditions of this services.")
    

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'arrival_date_time','agree_term']
        
        widgets = {
            'arrival_date_time': DateTimePickerInput(format='%m/%d/%Y %H:%M'),
        }
