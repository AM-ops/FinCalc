from django.conf.urls import url
from . import views

app_name = 'loan_app'

urlpatterns = [
    url(r'overview/$',views.LoanHomeView.as_view(), name='loan_index'),
    url(r'calculate/$',views.LoanCalcView.as_view(), name='calc_loan'),
    url(r'portfolio/$',views.LoanListView.as_view(), name='loan_list'),

    url(r'calculate/ConsLoanArrAV$',views.ConsLoanArrAVCreateView.as_view(), name='create_ConsLoanArrAV'),
    url(r'calculate/ConsLoanArrAV/(?P<pk>\d+)/$',views.ConsLoanArrAVDetailView.as_view(), name='ConsLoanArrAV_detail'),
    url(r'calculate/ConsLoanArrAV/delete/(?P<pk>\d+)/$',views.ConsLoanArrAVDeleteView.as_view(), name='ConsLoanArrAV_delete'),

    url(r'calculate/ConsLoanAdvAV$',views.ConsLoanAdvAVCreateView.as_view(), name='create_ConsLoanAdvAV'),
    url(r'calculate/ConsLoanAdvAV/(?P<pk>\d+)/$',views.ConsLoanAdvAVDetailView.as_view(), name='ConsLoanAdvAV_detail'),
    url(r'calculate/ConsLoanAdvAV/delete/(?P<pk>\d+)/$',views.ConsLoanAdvAVDeleteView.as_view(), name='ConsLoanAdvAV_delete'),

    url(r'calculate/IncLoanArrAV$',views.IncLoanArrAVCreateView.as_view(), name='create_IncLoanArrAV'),
    url(r'calculate/IncLoanArrAV/(?P<pk>\d+)/$',views.IncLoanArrAVDetailView.as_view(), name='IncLoanArrAV_detail'),
    url(r'calculate/IncLoanArrAV/delete/(?P<pk>\d+)/$',views.IncLoanArrAVDeleteView.as_view(), name='IncLoanArrAV_delete'),

    url(r'calculate/IncLoanAdvAV$',views.IncLoanAdvAVCreateView.as_view(), name='create_IncLoanAdvAV'),
    url(r'calculate/IncLoanAdvAV/(?P<pk>\d+)/$',views.IncLoanAdvAVDetailView.as_view(), name='IncLoanAdvAV_detail'),
    url(r'calculate/IncLoanAdvAV/delete/(?P<pk>\d+)/$',views.IncLoanAdvAVDeleteView.as_view(), name='IncLoanAdvAV_delete'),
]
