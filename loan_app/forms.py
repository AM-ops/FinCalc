#FinCalc\loan_app\forms.py
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import (ConsLoanArrAV, ConsLoanAdvAV, IncLoanAdvAV, IncLoanArrAV)
from django import forms

class ConsLoanArrAVModelForm(ModelForm):
    class Meta:
        model = ConsLoanArrAV
        fields = ['description','c','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Loan Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Payment/Withdrawal",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsLoanAdvAVModelForm(ModelForm):
    class Meta:
        model = ConsLoanAdvAV
        fields = ['description','c','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Loan Amount/Initial Investment Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Payment/Withdrawal",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class IncLoanArrAVModelForm(ModelForm):
    class Meta:
        model = IncLoanArrAV
        fields = ['description','c','x','i','j','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Payment/Withdrawal",
        "j": "Annual Increase in Installment (%)",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'j': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %, less than i'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class IncLoanAdvAVModelForm(ModelForm):
    class Meta:
        model = IncLoanAdvAV
        fields = ['description','c','x','i','j','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Payment/Withdrawal",
        "j": "Annual Increase in Installment (%)",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'j': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %, less than i'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
