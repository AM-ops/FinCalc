#FinCalc\loan_app\views.py
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
#from django.http import request
from . import models
from . import forms
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models.tools import HoverTool
from django.core.paginator import Paginator, EmptyPage

from .models import (ConsLoanArrAV, ConsLoanAdvAV, IncLoanAdvAV, IncLoanArrAV)
User = get_user_model()
# Create your views here.

class LoanHomeView(TemplateView):
    template_name = 'loan_app/loan_index.html'

class LoanCalcView(TemplateView):
    template_name = 'loan_app/calc_loan.html'

class LoanListView(LoginRequiredMixin,ListView):
     template_name = 'loan_app/loan_list.html'
     context_object_name = 'list'

     def get_queryset(self):
        queryset = ConsLoanArrAV.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = queryset.filter(user=username).order_by('description')
        return queryset

     def get_context_data(self, **kwargs):
        context = super(LoanListView, self).get_context_data(**kwargs)
        ConsLoanAdvAV_list = ConsLoanAdvAV.objects.all()
        IncLoanArrAV_list = IncLoanArrAV.objects.all()
        IncLoanAdvAV_list = IncLoanAdvAV.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            ConsLoanAdvAV_list = ConsLoanAdvAV_list.filter(user=username).order_by('description')
            IncLoanArrAV_list = IncLoanArrAV_list.filter(user=username).order_by('description')
            IncLoanAdvAV_list = IncLoanAdvAV_list.filter(user=username).order_by('description')
        context['ConsLoanAdvAV_list'] = ConsLoanAdvAV_list
        context['IncLoanArrAV_list'] = IncLoanArrAV_list
        context['IncLoanAdvAV_list'] = IncLoanAdvAV_list
        return context

class ConsLoanArrAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsLoanArrAVModelForm
    template_name = 'loan_app/ConsLoan/ConsLoanArrAV_form.html'
    model = models.ConsLoanArrAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsLoanArrAVDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsLoanArrAV
    context_object_name = 'detail'
    template_name = 'loan_app/ConsLoan/ConsLoanArrAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsLoanArrAVDetailView, self).get_context_data(**kwargs)
       curr = ConsLoanArrAV.objects.get(pk=self.object.pk)
       amort = []
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       ip = 1+i

       if ((n > 0) and (i > 0) and (c > 0)):
        for m in range(0,n):
            if(m==0):
                av = round(c,2)
                sr = 0
                sk = 0
                item = (m,av,sr,sk)
            else:
                av = round(((c*(ip**m)) - (x*(((ip**m)-1)/(i)))),2)
                sr = round((i * ((c*(ip**(m-1)) - (x*(((ip**(m-1))-1)/(i)))))),2)
                sk = round((x - sr),2)
                item = (m,av,sr,sk)
            amort.append(item)
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) - ( x * ( (((1+i)**j)-1)/i) ))
           l2 = list(t2)
           l2.append(ans)
           t2 = tuple(l2)


       	x =list(t1)
       	y =list(t2)
       	hover = HoverTool(mode='vline')
       	hover.tooltips = """
       	<div>
       	<h6>Amount: @y{0.00}</h6>
       	<h6>Year: @x</h6>
       	</div>
       	"""
       	plot = figure(title='Investment over Time', x_axis_label='Time in years', y_axis_label='Amount', plot_width=500, plot_height=500)
       	plot.add_tools(hover)
       	plot.line(x,y,line_width=2)
       	script, div = components(plot)
       	context['script'] = script
       	context['div'] = div
        p = Paginator(amort, 10)
        page_num = self.request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page=p.page(1)
        context['p'] = p
        context['items'] = page
       return context

class ConsLoanArrAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsLoanArrAV
    template_name = 'loan_app/ConsLoan/ConsLoanArrAV_delete.html'
    success_url = reverse_lazy('loan_app:loan_list')

class ConsLoanAdvAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsLoanAdvAVModelForm
    template_name = 'loan_app/ConsLoan/ConsLoanAdvAV_form.html'
    model = models.ConsLoanAdvAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsLoanAdvAVDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsLoanAdvAV
    context_object_name = 'detail'
    template_name = 'loan_app/ConsLoan/ConsLoanAdvAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsLoanAdvAVDetailView, self).get_context_data(**kwargs)
       curr = ConsLoanAdvAV.objects.get(pk=self.object.pk)
       amort =[]
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       ip = 1+i
       if ((n > 0) and (i > 0) and (c > 0)):
        for m in range(0,n):
            if(m==0):
                av = round(c,2)
                sr = 0
                sk = 0
                item = (m,av,sr,sk)
            else:
                av = round(((c*(ip**m)) - (x*ip*(((ip**m)-1)/(i)))),2)
                sr = round((i * ((c*(ip**(m-1)) - (x*ip*(((ip**(m-1))-1)/(i)))))),2)
                sk = round((x - sr),2)
                item = (m,av,sr,sk)
            amort.append(item)
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) - ( x * (1+i) * ( (((1+i)**j)-1)/i) ))
           l2 = list(t2)
           l2.append(ans)
           t2 = tuple(l2)

       	x =list(t1)
       	y =list(t2)
       	hover = HoverTool(mode='vline')
       	hover.tooltips = """
       	<div>
       	<h6>Amount: @y{0.00}</h6>
       	<h6>Year: @x</h6>
       	</div>
       	"""
       	plot = figure(title='Investment over Time', x_axis_label='Time in years', y_axis_label='Amount', plot_width=500, plot_height=500)
       	plot.add_tools(hover)
       	plot.line(x,y,line_width=2)
       	script, div = components(plot)
       	context['script'] = script
       	context['div'] = div
        p = Paginator(amort, 10)
        page_num = self.request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page=p.page(1)
        context['p'] = p
        context['items'] = page
       return context

class ConsLoanAdvAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsLoanAdvAV
    template_name = 'loan_app/ConsLoan/ConsLoanAdvAV_delete.html'
    success_url = reverse_lazy('loan_app:loan_list')

class IncLoanArrAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.IncLoanArrAVModelForm
    template_name = 'loan_app/IncLoan/IncLoanArrAV_form.html'
    model = models.IncLoanArrAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IncLoanArrAVDetailView(LoginRequiredMixin,DetailView):
    model = models.IncLoanArrAV
    context_object_name = 'detail'
    template_name = 'loan_app/IncLoan/IncLoanArrAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(IncLoanArrAVDetailView, self).get_context_data(**kwargs)
       curr = IncLoanArrAV.objects.get(pk=self.object.pk)
       amort=[]
       n = int(curr.n) + 1
       c = curr.c
       x = curr.x
       i = curr.i
       j = curr.j
       idi = curr.i/100
       iji = curr.j/100
       ip = 1+(curr.i/100)
       ij = 1+(curr.j/100)
       if((n>0) and (x>0) and (i>0) and (j>0) and (i>j) and (c > 0)):
        for m in range(0,n):
            if(m==0):
                av = round(c,2)
                sr = 0
                sk = 0
                item = (m,av,sr,sk)
            else:
                av = round(((c*(ip**m))-(x*((ip**m)-(ij**m))/(idi-iji))),2)
                sr = round((idi*((c*(ip**(m-1)))-(x*((ip**(m-1))-(ij**(m-1)))/(idi-iji)))),2)
                sk = round((x - sr),2)
                item = (m,av,sr,sk)
            amort.append(item)
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for k in range(0,n):
            ans = ((c*(ip**k))-(x*((ip**k)-(ij**k))/(idi-iji)))
       	    l2 = list(t2)
       	    l2.append(ans)
       	    t2 = tuple(l2)

       	x =list(t1)
       	y =list(t2)
       	hover = HoverTool(mode='vline')
       	hover.tooltips = """
       	<div>
       	<h6>Amount: @y{0.00}</h6>
       	<h6>Year: @x</h6>
       	</div>
       	"""
       	plot = figure(title='Investment over Time', x_axis_label='Time in years', y_axis_label='Amount', plot_width=500, plot_height=500)
       	plot.add_tools(hover)
       	plot.line(x,y,line_width=2)
       	script, div = components(plot)
       	context['script'] = script
       	context['div'] = div
        p = Paginator(amort, 10)
        page_num = self.request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page=p.page(1)
        context['p'] = p
        context['items'] = page
       return context

class IncLoanArrAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.IncLoanArrAV
    template_name = 'loan_app/IncLoan/IncLoanArrAV_delete.html'
    success_url = reverse_lazy('loan_app:loan_list')

class IncLoanAdvAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.IncLoanAdvAVModelForm
    template_name = 'loan_app/IncLoan/IncLoanAdvAV_form.html'
    model = models.IncLoanAdvAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IncLoanAdvAVDetailView(LoginRequiredMixin,DetailView):
    model = models.IncLoanAdvAV
    context_object_name = 'detail'
    template_name = 'loan_app/IncLoan/IncLoanAdvAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(IncLoanAdvAVDetailView, self).get_context_data(**kwargs)
       curr = IncLoanAdvAV.objects.get(pk=self.object.pk)
       amort=[]
       n = int(curr.n) + 1
       c = curr.c
       x = curr.x
       i = curr.i
       j = curr.j
       idi = curr.i/100
       iji = curr.j/100
       ip = 1+(curr.i/100)
       ij = 1+(curr.j/100)
       if((n>0) and (x>0) and (i>0) and (j>0) and (i>j) and (c > 0)):
        for m in range(0,n):
            if(m==0):
                av = round(c,2)
                sr = 0
                sk = 0
                item = (m,av,sr,sk)
            else:
                av = round(((c*(ip**m))-(x*ip*((ip**m)-(ij**m))/(idi-iji))),2)
                sr = round((idi*((c*(ip**(m-1)))-(x*ip*((ip**(m-1))-(ij**(m-1)))/(idi-iji)))),2)
                sk = round((x - sr),2)
                item = (m,av,sr,sk)
            amort.append(item)
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for k in range(0,n):
            ans = ((c*(ip**k))-(x*ip*((ip**k)-(ij**k))/(idi-iji)))
       	    l2 = list(t2)
       	    l2.append(ans)
       	    t2 = tuple(l2)

       	x =list(t1)
       	y =list(t2)
       	hover = HoverTool(mode='vline')
       	hover.tooltips = """
       	<div>
       	<h6>Amount: @y{0.00}</h6>
       	<h6>Year: @x</h6>
       	</div>
       	"""
       	plot = figure(title='Investment over Time', x_axis_label='Time in years', y_axis_label='Amount', plot_width=500, plot_height=500)
       	plot.add_tools(hover)
       	plot.line(x,y,line_width=2)
       	script, div = components(plot)
       	context['script'] = script
       	context['div'] = div
        p = Paginator(amort, 10)
        page_num = self.request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page=p.page(1)
        context['p'] = p
        context['items'] = page
       return context

class IncLoanAdvAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.IncLoanAdvAV
    template_name = 'loan_app/IncLoan/IncLoanAdvAV_delete.html'
    success_url = reverse_lazy('loan_app:loan_list')
