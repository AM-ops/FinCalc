#FinCalc\tvm_app\forms.py
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import (SingInvSimpAV, SingInvSimpPV, SingInvSimpN, SingInvSimpI, SingInvCompAV, SingInvCompPV,
SingInvCompN, SingInvCompI, ConsAnnuArrAV, ConsAnnuAdvAV, ConsAnnuPV, IncAnnuArrAV, IncAnnuAdvAV, IncAnnuPV,
ConsAnnuArrC, ConsAnnuArrX, ConsAnnuArrN, ConsAnnuAdvC, ConsAnnuAdvX, ConsAnnuAdvN)
from django import forms

class SingInvSimpAVModelForm(ModelForm):
    class Meta:
        model = SingInvSimpAV
        fields = ['description','c','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvSimpPVModelForm(ModelForm):
    class Meta:
        model = SingInvSimpPV
        fields = ['description','av','i','n']
        labels = {
        "av": "Accumulated Value",
        "i": "Annual Effective Interest Rate (%)",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvSimpNModelForm(ModelForm):
    class Meta:
        model = SingInvSimpN
        fields = ['description','av','pv','i']
        labels = {
        "av": "Accumulated Value",
        "pv": "Present Value",
        "i": "Annual Effective Interest Rate (%)",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pv': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvSimpIModelForm(ModelForm):
    class Meta:
        model = SingInvSimpI
        fields = ['description','av','pv','n']
        labels = {
        "av": "Accumulated Value",
        "pv": "Present Value",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as number %'}),
        'pv': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvCompAVModelForm(ModelForm):
    class Meta:
        model = SingInvCompAV
        fields = ['description','c','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvCompPVModelForm(ModelForm):
    class Meta:
        model = SingInvCompPV
        fields = ['description','av','i','n']
        labels = {
        "av": "Accumulated Value",
        "i": "Annual Effective Interest Rate (%)",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvCompNModelForm(ModelForm):
    class Meta:
        model = SingInvCompN
        fields = ['description','av','pv','i']
        labels = {
        "av": "Accumulated Value",
        "pv": "Present Value",
        "i": "Annual Effective Interest Rate (%)",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pv': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class SingInvCompIModelForm(ModelForm):
    class Meta:
        model = SingInvCompI
        fields = ['description','av','pv','n']
        labels = {
        "av": "Accumulated Value",
        "pv": "Present Value",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as number %'}),
        'pv': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuArrAVModelForm(ModelForm):
    class Meta:
        model = ConsAnnuArrAV
        fields = ['description','c','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
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

class ConsAnnuAdvAVModelForm(ModelForm):
    class Meta:
        model = ConsAnnuAdvAV
        fields = ['description','c','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
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

class ConsAnnuPVModelForm(ModelForm):
    class Meta:
        model = ConsAnnuPV
        fields = ['description','av','i','n']
        labels = {
        "av": "Accumulated Value",
        "i": "Annual Effective Interest Rate (%)",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class IncAnnuArrAVModelForm(ModelForm):
    class Meta:
        model = IncAnnuArrAV
        fields = ['description','c','x','i','j','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
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

class IncAnnuAdvAVModelForm(ModelForm):
    class Meta:
        model = IncAnnuAdvAV
        fields = ['description','c','x','i','j','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "c": "Initial Amount",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
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

class IncAnnuPVModelForm(ModelForm):
    class Meta:
        model = IncAnnuPV
        fields = ['description','av','i','n']
        labels = {
        "av": "Accumulated Value",
        "i": "Annual Effective Interest Rate (%)",
        "n": "Number of years",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuArrCModelForm(ModelForm):
    class Meta:
        model = ConsAnnuArrC
        fields = ['description','av','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuArrXModelForm(ModelForm):
    class Meta:
        model = ConsAnnuArrX
        fields = ['description','av','c','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "n": "Number of years",
        "description": "Description",
        "c": "Initial Amount",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuArrNModelForm(ModelForm):
    class Meta:
        model = ConsAnnuArrN
        fields = ['description','av','c','x','i']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "x": "Annuity Installment",
        "description": "Description",
        "c": "Initial Amount",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuAdvCModelForm(ModelForm):
    class Meta:
        model = ConsAnnuAdvC
        fields = ['description','av','x','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "n": "Number of years",
        "description": "Description",
        "x": "Annuity Installment",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuAdvXModelForm(ModelForm):
    class Meta:
        model = ConsAnnuAdvX
        fields = ['description','av','c','i','n']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "n": "Number of years",
        "description": "Description",
        "c": "Initial Amount",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'n': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class ConsAnnuAdvNModelForm(ModelForm):
    class Meta:
        model = ConsAnnuAdvN
        fields = ['description','av','c','x','i']
        labels = {
        "i": "Annual Effective Interest Rate (%)",
        "av": "Accumulated Value",
        "x": "Annuity Installment",
        "description": "Description",
        "c": "Initial Amount",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'x': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'av': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        'c': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a decimal e.g. 100.00'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
