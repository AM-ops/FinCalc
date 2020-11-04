#FinCalc\interest_app\models.py
from django.db import models
#from django.core.urlresolvers import reverse
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from math import log
from math import e
from decimal import Decimal

User = get_user_model()

class AEtoNP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Annual Effective to Nominal Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.p > 0:
            self.answer = (self.p * ( ((1+self.i/100)**(1/self.p)) - 1 ))*100
            self.idiv = self.i / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:AEtoNP_detail', kwargs={'pk':self.pk})

class AEtoEP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Annual Effective to Effective Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.p > 0:
            self.answer = (((1+self.i/100)**(1/self.p)) - 1)*100
            self.idiv = self.i / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:AEtoEP_detail', kwargs={'pk':self.pk})

class AEtoC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Annual Effective to Continuous Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (log(1+(self.i/100)))*100
        self.idiv = self.i / 100

    def get_absolute_url(self):
        return reverse('interest_app:AEtoC_detail', kwargs={'pk':self.pk})

class EPtoAE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Effective Per Period to Annual Effective Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.p > 0:
            self.idiv = self.ip / 100
            self.answer = (((1+(self.ip/100))**(self.p)) - 1)*100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:EPtoAE_detail', kwargs={'pk':self.pk})

class EPtoEP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pone = models.DecimalField(max_digits=20,decimal_places=5)
    ptwo = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Effective Per Period to Effective Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.ptwo > 0:
            self.answer = (((1+(self.ip/100))**(self.pone/self.ptwo)) - 1)*100
            self.idiv = self.ip / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:EPtoEP_detail', kwargs={'pk':self.pk})

class EPtoNP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pone = models.DecimalField(max_digits=20,decimal_places=5)
    ptwo = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Effective Per Period to Nominal Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.ptwo > 0:
            self.answer = (self.ptwo*(((1+(self.ip/100))**(self.pone/self.ptwo)) - 1))*100
            self.idiv = self.ip / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:EPtoNP_detail', kwargs={'pk':self.pk})

class EPtoC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Effective Per Period to Continuous Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (log((1+(self.i/100))**self.p))*100
        self.idiv = self.i / 100

    def get_absolute_url(self):
        return reverse('interest_app:EPtoC_detail', kwargs={'pk':self.pk})

class NPtoAE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Nominal Per Period to Annual Effective Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.p > 0:
            self.idiv = self.ip / 100
            self.answer = (((1+((self.ip/100)/self.p))**(self.p)) - 1)*100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:NPtoAE_detail', kwargs={'pk':self.pk})

class NPtoNP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pone = models.DecimalField(max_digits=20,decimal_places=5)
    ptwo = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Nominal Per Period to Nominal Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.ptwo > 0:
            self.answer = (self.ptwo*(((1+((self.ip/self.pone)/100))**(self.pone/self.ptwo)) - 1))*100
            self.idiv = self.ip / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:NPtoNP_detail', kwargs={'pk':self.pk})

class NPtoEP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pone = models.DecimalField(max_digits=20,decimal_places=5)
    ptwo = models.DecimalField(max_digits=20,decimal_places=5)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Nominal Per Period to Effective Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        if self.ptwo > 0:
            self.answer = (((1+((self.ip/self.pone)/100))**(self.pone/self.ptwo)) - 1)*100
            self.idiv = self.ip / 100
        else:
            self.answer = 0

    def get_absolute_url(self):
        return reverse('interest_app:NPtoEP_detail', kwargs={'pk':self.pk})

class NPtoC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ip = models.DecimalField(max_digits=20,decimal_places=5)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Nominal Per Period to Continuous Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (log((1+(self.ip/100/self.p))**self.p))*100
        self.idiv = self.ip / 100

    def get_absolute_url(self):
        return reverse('interest_app:NPtoC_detail', kwargs={'pk':self.pk})

class CtoAE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Continuous to Annual Effective Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (((Decimal(e)**(self.i/100)))-1)*100
        self.idiv = self.i / 100

    def get_absolute_url(self):
        return reverse('interest_app:CtoAE_detail', kwargs={'pk':self.pk})

class CtoEP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Continuous to Effective Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (((Decimal(e)**(self.i/100/self.p)))-1)*100
        self.idiv = self.i / 100

    def get_absolute_url(self):
        return reverse('interest_app:CtoEP_detail', kwargs={'pk':self.pk})

class CtoNP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    i = models.DecimalField(max_digits=20,decimal_places=5)
    p = models.DecimalField(max_digits=20,decimal_places=5)
    idiv = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    answer = models.DecimalField(max_digits=20,decimal_places=5, default=0)
    description = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50, default='Continuous to Nominal Per Period Rate')

    def save(self, *args, **kwargs):
        self.get_answer()
        super().save(*args, **kwargs)

    def get_answer(self, *args, **kwargs):
        self.answer = (self.p*(((Decimal(e)**(self.i/100/self.p)))-1))*100
        self.idiv = self.i / 100

    def get_absolute_url(self):
        return reverse('interest_app:CtoNP_detail', kwargs={'pk':self.pk})
