#FinCalc\interest_app\forms.py
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import AEtoNP, AEtoEP, AEtoC, EPtoAE, EPtoEP, EPtoNP, EPtoC, NPtoAE, NPtoNP, NPtoEP, NPtoC, CtoAE, CtoEP, CtoNP
from django import forms

#Model Form for Annual interest rate to Nominal interest rate
class AEtoNPModelForm(ModelForm):
    class Meta:
        model = AEtoNP
        fields = ['description','i','p']
        labels = {
        "i": "Annual Interest Rate (%)",
        "p": "Compounding Period",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AEtoEPModelForm(ModelForm):
    class Meta:
        model = AEtoEP
        fields = ['description','i','p']
        labels = {
        "i": "Annual Interest Rate (%)",
        "p": "Compounding Period",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AEtoCModelForm(ModelForm):
    class Meta:
        model = AEtoC
        fields = ['description','i']
        labels = {
        "i": "Annual Interest Rate (%)",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class EPtoAEModelForm(ModelForm):
    class Meta:
        model = EPtoAE
        fields = ['description','ip','p']
        labels = {
        "ip": "Effective Per Period Interest Rate (%)",
        "p": "Compounding Period",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class EPtoEPModelForm(ModelForm):
    class Meta:
        model = EPtoEP
        fields = ['description','ip','pone','ptwo']
        labels = {
        "ip": "Known Effective Per Period Interest Rate (%)",
        "pone": "Compounding Period for Known Interest Rate",
        "ptwo": "Compounding Period for Unknown Interest Rate",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        'ptwo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class EPtoNPModelForm(ModelForm):
    class Meta:
        model = EPtoNP
        fields = ['description','ip','pone','ptwo']
        labels = {
        "ip": "Known Effective Per Period Interest Rate (%)",
        "pone": "Compounding Period for Known Interest Rate",
        "ptwo": "Compounding Period for Unknown Interest Rate",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        'ptwo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class EPtoCModelForm(ModelForm):
    class Meta:
        model = EPtoC
        fields = ['description','i','p']
        labels = {
        "i": "Effective Per Period Rate (%)",
        "description": "Description",
        "p": "Compounding Period",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class NPtoAEModelForm(ModelForm):
    class Meta:
        model = NPtoAE
        fields = ['description','ip','p']
        labels = {
        "ip": "Nominal Per Period Interest Rate (%)",
        "p": "Compounding Period",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class NPtoNPModelForm(ModelForm):
    class Meta:
        model = NPtoNP
        fields = ['description','ip','pone','ptwo']
        labels = {
        "ip": "Known Nominal Per Period Interest Rate (%)",
        "pone": "Compounding Period for Known Interest Rate",
        "ptwo": "Compounding Period for Unknown Interest Rate",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        'ptwo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class NPtoEPModelForm(ModelForm):
    class Meta:
        model = NPtoEP
        fields = ['description','ip','pone','ptwo']
        labels = {
        "ip": "Known Nominal Per Period Interest Rate (%)",
        "pone": "Compounding Period for Known Interest Rate",
        "ptwo": "Compounding Period for Unknown Interest Rate",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'pone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        'ptwo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class NPtoCModelForm(ModelForm):
    class Meta:
        model = NPtoC
        fields = ['description','ip','p']
        labels = {
        "ip": "Nominal Per Period Interest Rate (%)",
        "description": "Description",
        "p": "Compounding Period",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'ip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class CtoAEModelForm(ModelForm):
    class Meta:
        model = CtoAE
        fields = ['description','i']
        labels = {
        "i": "Continuous Interest Rate (%)",
        "description": "Description",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class CtoEPModelForm(ModelForm):
    class Meta:
        model = CtoEP
        fields = ['description','i','p']
        labels = {
        "i": "Continuous Interest Rate (%)",
        "description": "Description",
        "p": "Compounding Period",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class CtoNPModelForm(ModelForm):
    class Meta:
        model = CtoNP
        fields = ['description','i','p']
        labels = {
        "i": "Continuous Interest Rate (%)",
        "description": "Description",
        "p": "Compounding Period",
        }
        widgets = {
        'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g. Question 1'}),
        'i': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a %'}),
        'p': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter as a number like 12 for monthly'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
