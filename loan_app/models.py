#FinCalc\loan_app\models.py
from django.db import models
#from django.core.urlresolvers import reverse
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
#from math import log
#from math import e
from decimal import Decimal
from sympy import symbols, Eq, solve

User = get_user_model()

# Create your models here.
class ConsLoanArrAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Constant Loan/Withdrawal with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.c > 0)):
            idi = self.i/100
            self.answer = (( self.c* ((1+idi)**self.n) ) - ( self.x * ( (((1+idi)**self.n)-1)/idi) ))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('loan_app:ConsLoanArrAV_detail', kwargs={'pk':self.pk})

class ConsLoanAdvAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Constant Loan/Withdrawal with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.c > 0)):
            idi = self.i/100
            self.answer = (( self.c* ((1+idi)**self.n) ) - ( self.x * (1+idi) * ( (((1+idi)**self.n)-1)/idi) ))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('loan_app:ConsLoanAdvAV_detail', kwargs={'pk':self.pk})

class IncLoanArrAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    j = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    jdiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Increasing Loan/Withdrawal with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.j>0) and (self.j<self.i) and (self.c > 0)):
            idi = self.i/100
            iji = self.j/100
            ip = 1+(self.i/100)
            ij = 1+(self.j/100)
            self.answer = ((self.c*(ip**self.n))-(self.x*((ip**self.n)-(ij**self.n))/(idi-iji)))
            self.idiv = self.i/100
            self.jdiv = self.j/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('loan_app:IncLoanArrAV_detail', kwargs={'pk':self.pk})

class IncLoanAdvAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    j = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    jdiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Increasing Loan/Withdrawal with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.j>0) and (self.j<self.i) and (self.c > 0)):
            idi = self.i/100
            iji = self.j/100
            ip = 1+(self.i/100)
            ij = 1+(self.j/100)
            self.answer = ((self.c*(ip**self.n))-(self.x*(ip)*((ip**self.n)-(ij**self.n))/(idi-iji)))
            self.idiv = self.i/100
            self.jdiv = self.j/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('loan_app:IncLoanAdvAV_detail', kwargs={'pk':self.pk})
