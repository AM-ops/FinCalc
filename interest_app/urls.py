#FinCalc\interest_app\urls.py
from django.conf.urls import url
from django.urls import path
from . import views
from . import models
from django.contrib import admin

app_name = 'interest_app'

urlpatterns = [
    url(r'overview/$',views.InterestHomeView.as_view(), name='interest_index'),
    url(r'portfolio/$',views.InterestListView.as_view(), name='interest_list'),
    url(r'calculate/$',views.InterestCalcView.as_view(), name='calc_interest'),
    url(r'calculate/AEtoNP$',views.AEtoNPCreateView.as_view(), name='create_AEtoNP'),
    url(r'calculate/AEtoNP/(?P<pk>\d+)/$',views.AEtoNPDetailView.as_view(), name='AEtoNP_detail'),
    url(r'calculate/AEtoNP/delete/(?P<pk>\d+)/$',views.AEtoNPDeleteView.as_view(), name='AEtoNP_delete'),
    url(r'calculate/AEtoEP$',views.AEtoEPCreateView.as_view(), name='create_AEtoEP'),
    url(r'calculate/AEtoEP/(?P<pk>\d+)/$',views.AEtoEPDetailView.as_view(), name='AEtoEP_detail'),
    url(r'calculate/AEtoEP/delete/(?P<pk>\d+)/$',views.AEtoEPDeleteView.as_view(), name='AEtoEP_delete'),
    url(r'calculate/AEtoC$',views.AEtoCCreateView.as_view(), name='create_AEtoC'),
    url(r'calculate/AEtoC/(?P<pk>\d+)/$',views.AEtoCDetailView.as_view(), name='AEtoC_detail'),
    url(r'calculate/AEtoC/delete/(?P<pk>\d+)/$',views.AEtoCDeleteView.as_view(), name='AEtoC_delete'),
    url(r'calculate/EPtoAE$',views.EPtoAECreateView.as_view(), name='create_EPtoAE'),
    url(r'calculate/EPtoAE/(?P<pk>\d+)/$',views.EPtoAEDetailView.as_view(), name='EPtoAE_detail'),
    url(r'calculate/EPtoAE/delete/(?P<pk>\d+)/$',views.EPtoAEDeleteView.as_view(), name='EPtoAE_delete'),
    url(r'calculate/EPtoEP$',views.EPtoEPCreateView.as_view(), name='create_EPtoEP'),
    url(r'calculate/EPtoEP/(?P<pk>\d+)/$',views.EPtoEPDetailView.as_view(), name='EPtoEP_detail'),
    url(r'calculate/EPtoEP/delete/(?P<pk>\d+)/$',views.EPtoEPDeleteView.as_view(), name='EPtoEP_delete'),
    url(r'calculate/EPtoNP$',views.EPtoNPCreateView.as_view(), name='create_EPtoNP'),
    url(r'calculate/EPtoNP/(?P<pk>\d+)/$',views.EPtoNPDetailView.as_view(), name='EPtoNP_detail'),
    url(r'calculate/EPtoNP/delete/(?P<pk>\d+)/$',views.EPtoNPDeleteView.as_view(), name='EPtoNP_delete'),
    url(r'calculate/EPtoC$',views.EPtoCCreateView.as_view(), name='create_EPtoC'),
    url(r'calculate/EPtoC/(?P<pk>\d+)/$',views.EPtoCDetailView.as_view(), name='EPtoC_detail'),
    url(r'calculate/EPtoC/delete/(?P<pk>\d+)/$',views.EPtoCDeleteView.as_view(), name='EPtoC_delete'),
    url(r'calculate/NPtoAE$',views.NPtoAECreateView.as_view(), name='create_NPtoAE'),
    url(r'calculate/NPtoAE/(?P<pk>\d+)/$',views.NPtoAEDetailView.as_view(), name='NPtoAE_detail'),
    url(r'calculate/NPtoAE/delete/(?P<pk>\d+)/$',views.NPtoAEDeleteView.as_view(), name='NPtoAE_delete'),
    url(r'calculate/NPtoNP$',views.NPtoNPCreateView.as_view(), name='create_NPtoNP'),
    url(r'calculate/NPtoNP/(?P<pk>\d+)/$',views.NPtoNPDetailView.as_view(), name='NPtoNP_detail'),
    url(r'calculate/NPtoNP/delete/(?P<pk>\d+)/$',views.NPtoNPDeleteView.as_view(), name='NPtoNP_delete'),
    url(r'calculate/NPtoEP$',views.NPtoEPCreateView.as_view(), name='create_NPtoEP'),
    url(r'calculate/NPtoEP/(?P<pk>\d+)/$',views.NPtoEPDetailView.as_view(), name='NPtoEP_detail'),
    url(r'calculate/NPtoEP/delete/(?P<pk>\d+)/$',views.NPtoEPDeleteView.as_view(), name='NPtoEP_delete'),
    url(r'calculate/NPtoC$',views.NPtoCCreateView.as_view(), name='create_NPtoC'),
    url(r'calculate/NPtoC/(?P<pk>\d+)/$',views.NPtoCDetailView.as_view(), name='NPtoC_detail'),
    url(r'calculate/NPtoC/delete/(?P<pk>\d+)/$',views.NPtoCDeleteView.as_view(), name='NPtoC_delete'),
    url(r'calculate/CtoAE$',views.CtoAECreateView.as_view(), name='create_CtoAE'),
    url(r'calculate/CtoAE/(?P<pk>\d+)/$',views.CtoAEDetailView.as_view(), name='CtoAE_detail'),
    url(r'calculate/CtoAE/delete/(?P<pk>\d+)/$',views.CtoAEDeleteView.as_view(), name='CtoAE_delete'),
    url(r'calculate/CtoEP$',views.CtoEPCreateView.as_view(), name='create_CtoEP'),
    url(r'calculate/CtoEP/(?P<pk>\d+)/$',views.CtoEPDetailView.as_view(), name='CtoEP_detail'),
    url(r'calculate/CtoEP/delete/(?P<pk>\d+)/$',views.CtoEPDeleteView.as_view(), name='CtoEP_delete'),
    url(r'calculate/CtoNP$',views.CtoNPCreateView.as_view(), name='create_CtoNP'),
    url(r'calculate/CtoNP/(?P<pk>\d+)/$',views.CtoNPDetailView.as_view(), name='CtoNP_detail'),
    url(r'calculate/CtoNP/delete/(?P<pk>\d+)/$',views.CtoNPDeleteView.as_view(), name='CtoNP_delete'),

]
