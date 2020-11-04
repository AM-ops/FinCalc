from django.conf.urls import url
from . import views

app_name = 'tvm_app'

urlpatterns = [
    url(r'overview/$',views.TVMHomeView.as_view(), name='tvm_index'),
    url(r'portfolio/$',views.TVMListView.as_view(), name='tvm_list'),
    url(r'calculate/$',views.TVMCalcView.as_view(), name='calc_tvm'),
    url(r'calculate/SingInvSimpAV$',views.SingInvSimpAVCreateView.as_view(), name='create_SingInvSimpAV'),
    url(r'calculate/SingInvSimpAV/(?P<pk>\d+)/$',views.SingInvSimpAVDetailView.as_view(), name='SingInvSimpAV_detail'),
    url(r'calculate/SingInvSimpAV/delete/(?P<pk>\d+)/$',views.SingInvSimpAVDeleteView.as_view(), name='SingInvSimpAV_delete'),
    url(r'calculate/SingInvSimpPV$',views.SingInvSimpPVCreateView.as_view(), name='create_SingInvSimpPV'),
    url(r'calculate/SingInvSimpPV/(?P<pk>\d+)/$',views.SingInvSimpPVDetailView.as_view(), name='SingInvSimpPV_detail'),
    url(r'calculate/SingInvSimpPV/delete/(?P<pk>\d+)/$',views.SingInvSimpPVDeleteView.as_view(), name='SingInvSimpPV_delete'),
    url(r'calculate/SingInvSimpN$',views.SingInvSimpNCreateView.as_view(), name='create_SingInvSimpN'),
    url(r'calculate/SingInvSimpN/(?P<pk>\d+)/$',views.SingInvSimpNDetailView.as_view(), name='SingInvSimpN_detail'),
    url(r'calculate/SingInvSimpN/delete/(?P<pk>\d+)/$',views.SingInvSimpNDeleteView.as_view(), name='SingInvSimpN_delete'),
    url(r'calculate/SingInvSimpI$',views.SingInvSimpICreateView.as_view(), name='create_SingInvSimpI'),
    url(r'calculate/SingInvSimpI/(?P<pk>\d+)/$',views.SingInvSimpIDetailView.as_view(), name='SingInvSimpI_detail'),
    url(r'calculate/SingInvSimpI/delete/(?P<pk>\d+)/$',views.SingInvSimpIDeleteView.as_view(), name='SingInvSimpI_delete'),
    url(r'calculate/SingInvCompAV$',views.SingInvCompAVCreateView.as_view(), name='create_SingInvCompAV'),
    url(r'calculate/SingInvCompAV/(?P<pk>\d+)/$',views.SingInvCompAVDetailView.as_view(), name='SingInvCompAV_detail'),
    url(r'calculate/SingInvCompAV/delete/(?P<pk>\d+)/$',views.SingInvCompAVDeleteView.as_view(), name='SingInvCompAV_delete'),
    url(r'calculate/SingInvCompPV$',views.SingInvCompPVCreateView.as_view(), name='create_SingInvCompPV'),
    url(r'calculate/SingInvCompPV/(?P<pk>\d+)/$',views.SingInvCompPVDetailView.as_view(), name='SingInvCompPV_detail'),
    url(r'calculate/SingInvCompPV/delete/(?P<pk>\d+)/$',views.SingInvCompPVDeleteView.as_view(), name='SingInvCompPV_delete'),
    url(r'calculate/SingInvCompN$',views.SingInvCompNCreateView.as_view(), name='create_SingInvCompN'),
    url(r'calculate/SingInvCompN/(?P<pk>\d+)/$',views.SingInvCompNDetailView.as_view(), name='SingInvCompN_detail'),
    url(r'calculate/SingInvCompN/delete/(?P<pk>\d+)/$',views.SingInvCompNDeleteView.as_view(), name='SingInvCompN_delete'),
    url(r'calculate/SingInvCompI$',views.SingInvCompICreateView.as_view(), name='create_SingInvCompI'),
    url(r'calculate/SingInvCompI/(?P<pk>\d+)/$',views.SingInvCompIDetailView.as_view(), name='SingInvCompI_detail'),
    url(r'calculate/SingInvCompI/delete/(?P<pk>\d+)/$',views.SingInvCompIDeleteView.as_view(), name='SingInvCompI_delete'),

    url(r'calculate/ConsAnnuArrAV$',views.ConsAnnuArrAVCreateView.as_view(), name='create_ConsAnnuArrAV'),
    url(r'calculate/ConsAnnuArrAV/(?P<pk>\d+)/$',views.ConsAnnuArrAVDetailView.as_view(), name='ConsAnnuArrAV_detail'),
    url(r'calculate/ConsAnnuArrAV/delete/(?P<pk>\d+)/$',views.ConsAnnuArrAVDeleteView.as_view(), name='ConsAnnuArrAV_delete'),

    url(r'calculate/ConsAnnuArrC$',views.ConsAnnuArrCCreateView.as_view(), name='create_ConsAnnuArrC'),
    url(r'calculate/ConsAnnuArrC/(?P<pk>\d+)/$',views.ConsAnnuArrCDetailView.as_view(), name='ConsAnnuArrC_detail'),
    url(r'calculate/ConsAnnuArrC/delete/(?P<pk>\d+)/$',views.ConsAnnuArrCDeleteView.as_view(), name='ConsAnnuArrC_delete'),

    url(r'calculate/ConsAnnuArrX$',views.ConsAnnuArrXCreateView.as_view(), name='create_ConsAnnuArrX'),
    url(r'calculate/ConsAnnuArrX/(?P<pk>\d+)/$',views.ConsAnnuArrXDetailView.as_view(), name='ConsAnnuArrX_detail'),
    url(r'calculate/ConsAnnuArrX/delete/(?P<pk>\d+)/$',views.ConsAnnuArrXDeleteView.as_view(), name='ConsAnnuArrX_delete'),

    url(r'calculate/ConsAnnuArrN$',views.ConsAnnuArrNCreateView.as_view(), name='create_ConsAnnuArrN'),
    url(r'calculate/ConsAnnuArrN/(?P<pk>\d+)/$',views.ConsAnnuArrNDetailView.as_view(), name='ConsAnnuArrN_detail'),
    url(r'calculate/ConsAnnuArrN/delete/(?P<pk>\d+)/$',views.ConsAnnuArrNDeleteView.as_view(), name='ConsAnnuArrN_delete'),

    url(r'calculate/ConsAnnuAdvAV$',views.ConsAnnuAdvAVCreateView.as_view(), name='create_ConsAnnuAdvAV'),
    url(r'calculate/ConsAnnuAdvAV/(?P<pk>\d+)/$',views.ConsAnnuAdvAVDetailView.as_view(), name='ConsAnnuAdvAV_detail'),
    url(r'calculate/ConsAnnuAdvAV/delete/(?P<pk>\d+)/$',views.ConsAnnuAdvAVDeleteView.as_view(), name='ConsAnnuAdvAV_delete'),

    url(r'calculate/ConsAnnuAdvC$',views.ConsAnnuAdvCCreateView.as_view(), name='create_ConsAnnuAdvC'),
    url(r'calculate/ConsAnnuAdvC/(?P<pk>\d+)/$',views.ConsAnnuAdvCDetailView.as_view(), name='ConsAnnuAdvC_detail'),
    url(r'calculate/ConsAnnuAdvC/delete/(?P<pk>\d+)/$',views.ConsAnnuAdvCDeleteView.as_view(), name='ConsAnnuAdvC_delete'),

    url(r'calculate/ConsAnnuAdvX$',views.ConsAnnuAdvXCreateView.as_view(), name='create_ConsAnnuAdvX'),
    url(r'calculate/ConsAnnuAdvX/(?P<pk>\d+)/$',views.ConsAnnuAdvXDetailView.as_view(), name='ConsAnnuAdvX_detail'),
    url(r'calculate/ConsAnnuAdvX/delete/(?P<pk>\d+)/$',views.ConsAnnuAdvXDeleteView.as_view(), name='ConsAnnuAdvX_delete'),

    url(r'calculate/ConsAnnuAdvN$',views.ConsAnnuAdvNCreateView.as_view(), name='create_ConsAnnuAdvN'),
    url(r'calculate/ConsAnnuAdvN/(?P<pk>\d+)/$',views.ConsAnnuAdvNDetailView.as_view(), name='ConsAnnuAdvN_detail'),
    url(r'calculate/ConsAnnuAdvN/delete/(?P<pk>\d+)/$',views.ConsAnnuAdvNDeleteView.as_view(), name='ConsAnnuAdvN_delete'),

    url(r'calculate/ConsAnnuPV$',views.ConsAnnuPVCreateView.as_view(), name='create_ConsAnnuPV'),
    url(r'calculate/ConsAnnuPV/(?P<pk>\d+)/$',views.ConsAnnuPVDetailView.as_view(), name='ConsAnnuPV_detail'),
    url(r'calculate/ConsAnnuPV/delete/(?P<pk>\d+)/$',views.ConsAnnuPVDeleteView.as_view(), name='ConsAnnuPV_delete'),

    url(r'calculate/IncAnnuArrAV$',views.IncAnnuArrAVCreateView.as_view(), name='create_IncAnnuArrAV'),
    url(r'calculate/IncAnnuArrAV/(?P<pk>\d+)/$',views.IncAnnuArrAVDetailView.as_view(), name='IncAnnuArrAV_detail'),
    url(r'calculate/IncAnnuArrAV/delete/(?P<pk>\d+)/$',views.IncAnnuArrAVDeleteView.as_view(), name='IncAnnuArrAV_delete'),

    url(r'calculate/IncAnnuAdvAV$',views.IncAnnuAdvAVCreateView.as_view(), name='create_IncAnnuAdvAV'),
    url(r'calculate/IncAnnuAdvAV/(?P<pk>\d+)/$',views.IncAnnuAdvAVDetailView.as_view(), name='IncAnnuAdvAV_detail'),
    url(r'calculate/IncAnnuAdvAV/delete/(?P<pk>\d+)/$',views.IncAnnuAdvAVDeleteView.as_view(), name='IncAnnuAdvAV_delete'),

    url(r'calculate/IncAnnuPV$',views.IncAnnuPVCreateView.as_view(), name='create_IncAnnuPV'),
    url(r'calculate/IncAnnuPV/(?P<pk>\d+)/$',views.IncAnnuPVDetailView.as_view(), name='IncAnnuPV_detail'),
    url(r'calculate/IncAnnuPV/delete/(?P<pk>\d+)/$',views.IncAnnuPVDeleteView.as_view(), name='IncAnnuPV_delete'),
]
