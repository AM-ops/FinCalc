#FinCalc\interest_app\admin.py
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.AEtoNP)
admin.site.register(models.AEtoEP)
admin.site.register(models.AEtoC)
admin.site.register(models.EPtoAE)
admin.site.register(models.EPtoEP)
admin.site.register(models.EPtoNP)
admin.site.register(models.EPtoC)
admin.site.register(models.NPtoAE)
admin.site.register(models.NPtoNP)
admin.site.register(models.NPtoEP)
admin.site.register(models.NPtoC)
admin.site.register(models.CtoAE)
admin.site.register(models.CtoEP)
admin.site.register(models.CtoNP)
