#FinCalc\tvm_app\admin.py
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SingInvSimpAV)
admin.site.register(models.SingInvSimpPV)
admin.site.register(models.SingInvSimpN)
admin.site.register(models.SingInvSimpI)
admin.site.register(models.SingInvCompAV)
admin.site.register(models.SingInvCompPV)
admin.site.register(models.SingInvCompN)
admin.site.register(models.SingInvCompI)
admin.site.register(models.ConsAnnuArrAV)
admin.site.register(models.ConsAnnuArrC)
admin.site.register(models.ConsAnnuArrX)
admin.site.register(models.ConsAnnuAdvAV)
admin.site.register(models.ConsAnnuAdvC)
admin.site.register(models.ConsAnnuAdvX)
admin.site.register(models.ConsAnnuPV)
admin.site.register(models.IncAnnuArrAV)
admin.site.register(models.IncAnnuAdvAV)
admin.site.register(models.ConsAnnuArrN)
admin.site.register(models.ConsAnnuAdvN)
