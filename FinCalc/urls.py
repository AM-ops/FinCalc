#FinCalc\FinCalc\urls.py
"""FinCalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import urls as u
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include(u)),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^contact/$',views.ContactPage.as_view(),name='contact'),
    url(r'^interest/',include('interest_app.urls',namespace='interest_app')),
    url(r'^loan/',include('loan_app.urls',namespace='loan_app')),
    url(r'^tvm/',include('tvm_app.urls',namespace='tvm_app')),
]
