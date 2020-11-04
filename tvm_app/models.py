#FinCalc\tvm_app\models.py
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

class SingInvSimpAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Single Investment with Simple Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            self.answer = self.c*(1+(self.i/100)*self.n)
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvSimpAV_detail', kwargs={'pk':self.pk})

class SingInvSimpPV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='PV for Single Investment with Simple Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            self.answer = self.av*((1+(self.i/100)*self.n)**-1)
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvSimpPV_detail', kwargs={'pk':self.pk})

class SingInvSimpN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    pv = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='n for Single Investment with Simple Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.pv > 0) and (self.av > 0) and (self.i > 0)):
            self.answer = ((self.av/self.pv)-1)/(self.i/100)
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvSimpN_detail', kwargs={'pk':self.pk})

class SingInvSimpI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    pv = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='i for Single Investment with Simple Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.pv > 0) and (self.av > 0) and (self.n > 0)):
            self.answer = (((self.av/self.pv)-1)/(self.n/100))*100
            self.idiv = self.answer/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvSimpI_detail', kwargs={'pk':self.pk})

class SingInvCompAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Single Investment with Compound Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            self.answer = self.c*((1+(self.i/100))**self.n)
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvCompAV_detail', kwargs={'pk':self.pk})

class SingInvCompPV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='PV for Single Investment with Compound Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            self.answer = self.av*((1+(self.i/100))**(-1*self.n))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvCompPV_detail', kwargs={'pk':self.pk})

class SingInvCompN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    pv = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='n for Single Investment with Compound Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.pv > 0) and (self.av > 0) and (self.i > 0)):
            n = symbols('n')
            eq1 = Eq(self.av,(self.pv*((1+(self.i/100))**n)))
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvCompN_detail', kwargs={'pk':self.pk})

class SingInvCompI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    pv = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='i for Single Investment with Compound Interest')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.pv > 0) and (self.av > 0) and (self.n > 0)):
            i = symbols('i')
            eq1 = Eq(i, ((self.av/self.pv)**(1/self.n))-1)
            sol = solve(eq1)
            s = sol[0]*100
            self.answer = Decimal(str(format(s,'.5f')))
            self.idiv = Decimal(str(format(sol[0],'.5f')))
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:SingInvCompI_detail', kwargs={'pk':self.pk})

class ConsAnnuArrAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Constant Annuity with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0)):
            idi = self.i/100
            self.answer = (( self.c* ((1+idi)**self.n) ) + ( self.x * ( (((1+idi)**self.n)-1)/idi) ))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuArrAV_detail', kwargs={'pk':self.pk})

class ConsAnnuAdvAV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='AV for Constant Annuity with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0)):
            idi = self.i/100
            self.answer = (( self.c* ((1+idi)**self.n) ) + ( self.x * (1+idi) * ( (((1+idi)**self.n)-1)/idi) ))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuAdvAV_detail', kwargs={'pk':self.pk})

class ConsAnnuPV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='PV for Constant Annuity')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            idi = self.i/100
            self.answer = (self.av * ((1+(self.i/100))**(-self.n)) )
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuPV_detail', kwargs={'pk':self.pk})

class IncAnnuArrAV(models.Model):
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
    type = models.CharField(max_length=50, default='AV for Increasing Annuity with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.j>0) and (self.j<self.i)):
            idi = self.i/100
            iji = self.j/100
            ip = 1+(self.i/100)
            ij = 1+(self.j/100)
            self.answer = ((self.c*(ip**self.n))+(self.x*((ip**self.n)-(ij**self.n))/(idi-iji)))
            self.idiv = self.i/100
            self.jdiv = self.j/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:IncAnnuArrAV_detail', kwargs={'pk':self.pk})

class IncAnnuAdvAV(models.Model):
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
    type = models.CharField(max_length=50, default='AV for Increasing Annuity with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.j>0) and (self.j<self.i)):
            idi = self.i/100
            iji = self.j/100
            ip = 1+(self.i/100)
            ij = 1+(self.j/100)
            self.answer = ((self.c*(ip**self.n))+(self.x*(ip)*((ip**self.n)-(ij**self.n))/(idi-iji)))
            self.idiv = self.i/100
            self.jdiv = self.j/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:IncAnnuAdvAV_detail', kwargs={'pk':self.pk})

class IncAnnuPV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='PV for Increasing Annuity')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0)):
            idi = self.i/100
            self.answer = (self.av * ((1+(self.i/100))**(-self.n)) )
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:IncAnnuPV_detail', kwargs={'pk':self.pk})

class ConsAnnuArrC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Initial Investment for Constant Annuity with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.av>0)):
            c = symbols('c')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (c*(ip**self.n))+(self.x*((ip**self.n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuArrC_detail', kwargs={'pk':self.pk})

class ConsAnnuArrX(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Installment for Constant Annuity with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.av>0)):
            x = symbols('x')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (self.c*(ip**self.n))+(x*((ip**self.n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuArrX_detail', kwargs={'pk':self.pk})

class ConsAnnuArrN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Period for Constant Annuity with Interest Paid in Arrears')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.x > 0) and (self.i > 0) and (self.av>0)):
            n = symbols('n')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (self.c*(ip**n))+(self.x*((ip**n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuArrN_detail', kwargs={'pk':self.pk})

class ConsAnnuAdvC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Initial Investment for Constant Annuity with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.x > 0) and (self.av>0)):
            c = symbols('c')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (c*(ip**self.n))+(self.x*ip*((ip**self.n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuAdvC_detail', kwargs={'pk':self.pk})

class ConsAnnuAdvX(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    n = models.DecimalField(max_digits=20,decimal_places=5)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Installment for Constant Annuity with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.n > 0) and (self.i > 0) and (self.av>0)):
            x = symbols('x')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (self.c*(ip**self.n))+(x*ip*((ip**self.n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuAdvX_detail', kwargs={'pk':self.pk})

class ConsAnnuAdvN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    av = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    x = models.DecimalField(max_digits=20,decimal_places=5)
    c = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Period for Constant Annuity with Interest Paid in Advance')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if ((self.x > 0) and (self.i > 0) and (self.av>0)):
            n = symbols('n')
            ip = (1+(self.i/100))
            idi = self.i/100
            eq1 = Eq(( (self.c*(ip**n))+(self.x*ip*((ip**n)-1)/idi)-self.av ),0)
            sol = solve(eq1)
            self.answer = Decimal(str(format(sol[0],'.5f')))
            self.idiv = self.i/100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('tvm_app:ConsAnnuAdvN_detail', kwargs={'pk':self.pk})
