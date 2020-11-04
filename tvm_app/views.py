#FinCalc\tvm_app\views.py
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

from .models import (SingInvSimpAV, SingInvSimpPV, SingInvSimpN, SingInvSimpI, SingInvCompAV,
SingInvCompPV, SingInvCompN, SingInvCompI, ConsAnnuArrAV, ConsAnnuAdvAV, ConsAnnuPV, IncAnnuArrAV,IncAnnuAdvAV,
IncAnnuPV, ConsAnnuArrC, ConsAnnuArrX, ConsAnnuAdvC, ConsAnnuAdvX, ConsAnnuArrN, ConsAnnuAdvN)
User = get_user_model()
# Create your views here.

class TVMHomeView(TemplateView):
    template_name = 'tvm_app/tvm_index.html'

class TVMCalcView(LoginRequiredMixin,TemplateView):
    template_name = 'tvm_app/calc_tvm.html'

class TVMListView(LoginRequiredMixin,ListView):
     template_name = 'tvm_app/tvm_list.html'
     context_object_name = 'list'

     def get_queryset(self):
        queryset = SingInvSimpAV.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = queryset.filter(user=username).order_by('description')
        return queryset

     def get_context_data(self, **kwargs):
        context = super(TVMListView, self).get_context_data(**kwargs)
        SingInvSimpAV_list = SingInvSimpAV.objects.all()
        SingInvSimpPV_list = SingInvSimpPV.objects.all()
        SingInvSimpN_list = SingInvSimpN.objects.all()
        SingInvSimpI_list = SingInvSimpI.objects.all()
        SingInvCompAV_list = SingInvCompAV.objects.all()
        SingInvCompPV_list = SingInvCompPV.objects.all()
        SingInvCompN_list = SingInvCompN.objects.all()
        SingInvCompI_list = SingInvCompI.objects.all()
        ConsAnnuArrAV_list = ConsAnnuArrAV.objects.all()
        ConsAnnuArrC_list = ConsAnnuArrC.objects.all()
        ConsAnnuArrX_list = ConsAnnuArrX.objects.all()
        ConsAnnuArrN_list = ConsAnnuArrN.objects.all()
        ConsAnnuAdvAV_list = ConsAnnuAdvAV.objects.all()
        ConsAnnuAdvC_list = ConsAnnuAdvC.objects.all()
        ConsAnnuAdvX_list = ConsAnnuAdvX.objects.all()
        ConsAnnuAdvN_list = ConsAnnuAdvN.objects.all()
        ConsAnnuPV_list = ConsAnnuPV.objects.all()
        IncAnnuArrAV_list = IncAnnuArrAV.objects.all()
        IncAnnuAdvAV_list = IncAnnuAdvAV.objects.all()
        IncAnnuPV_list = IncAnnuPV.objects.all()
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            SingInvSimpAV_list = SingInvSimpAV_list.filter(user=username).order_by('description')
            SingInvSimpPV_list = SingInvSimpPV_list.filter(user=username).order_by('description')
            SingInvSimpN_list = SingInvSimpN_list.filter(user=username).order_by('description')
            SingInvSimpI_list = SingInvSimpI_list.filter(user=username).order_by('description')
            SingInvCompAV_list = SingInvCompAV_list.filter(user=username).order_by('description')
            SingInvCompPV_list = SingInvCompPV_list.filter(user=username).order_by('description')
            SingInvCompN_list = SingInvCompN_list.filter(user=username).order_by('description')
            SingInvCompI_list = SingInvCompI_list.filter(user=username).order_by('description')
            ConsAnnuArrAV_list = ConsAnnuArrAV_list.filter(user=username).order_by('description')
            ConsAnnuArrC_list = ConsAnnuArrC_list.filter(user=username).order_by('description')
            ConsAnnuArrX_list = ConsAnnuArrX_list.filter(user=username).order_by('description')
            ConsAnnuArrN_list = ConsAnnuArrN_list.filter(user=username).order_by('description')
            ConsAnnuAdvAV_list = ConsAnnuAdvAV_list.filter(user=username).order_by('description')
            ConsAnnuAdvC_list = ConsAnnuAdvC_list.filter(user=username).order_by('description')
            ConsAnnuAdvX_list = ConsAnnuAdvX_list.filter(user=username).order_by('description')
            ConsAnnuAdvN_list = ConsAnnuAdvN_list.filter(user=username).order_by('description')
            ConsAnnuPV_list = ConsAnnuPV_list.filter(user=username).order_by('description')
            IncAnnuArrAV_list = IncAnnuArrAV_list.filter(user=username).order_by('description')
            IncAnnuAdvAV_list = IncAnnuAdvAV_list.filter(user=username).order_by('description')
            IncAnnuPV_list = IncAnnuPV_list.filter(user=username).order_by('description')
        context['SingInvSimpAV_list'] = SingInvSimpAV_list
        context['SingInvSimpPV_list'] = SingInvSimpPV_list
        context['SingInvSimpN_list'] = SingInvSimpN_list
        context['SingInvSimpI_list'] = SingInvSimpI_list
        context['SingInvCompAV_list'] = SingInvCompAV_list
        context['SingInvCompPV_list'] = SingInvCompPV_list
        context['SingInvCompN_list'] = SingInvCompN_list
        context['SingInvCompI_list'] = SingInvCompI_list
        context['ConsAnnuArrAV_list'] = ConsAnnuArrAV_list
        context['ConsAnnuArrC_list'] = ConsAnnuArrC_list
        context['ConsAnnuArrX_list'] = ConsAnnuArrX_list
        context['ConsAnnuArrN_list'] = ConsAnnuArrN_list
        context['ConsAnnuAdvAV_list'] = ConsAnnuAdvAV_list
        context['ConsAnnuAdvC_list'] = ConsAnnuAdvC_list
        context['ConsAnnuAdvX_list'] = ConsAnnuAdvX_list
        context['ConsAnnuAdvN_list'] = ConsAnnuAdvN_list
        context['ConsAnnuPV_list'] = ConsAnnuPV_list
        context['IncAnnuArrAV_list'] = IncAnnuArrAV_list
        context['IncAnnuAdvAV_list'] = IncAnnuAdvAV_list
        context['IncAnnuPV_list'] = IncAnnuPV_list
        return context

class SingInvSimpAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvSimpAVModelForm
    template_name = 'tvm_app/SingInvSimp/SingInvSimpAV_form.html'
    model = models.SingInvSimpAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvSimpAVDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvSimpAV
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvSimp/SingInvSimpAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvSimpAVDetailView, self).get_context_data(**kwargs)
       curr = SingInvSimpAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i
       if ((n > 0) and (c > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           	ans = c*(1+(i/100)*j)
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
       return context

class SingInvSimpAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvSimpAV
    template_name = 'tvm_app/SingInvSimp/SingInvSimpAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvSimpPVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvSimpPVModelForm
    template_name = 'tvm_app/SingInvSimp/SingInvSimpPV_form.html'
    model = models.SingInvSimpPV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvSimpPVDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvSimpPV
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvSimp/SingInvSimpPV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvSimpPVDetailView, self).get_context_data(**kwargs)
       curr = SingInvSimpPV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       av = curr.av
       i = curr.i
       if((n>0) and (av>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = av*((1+(i/100)*j)**-1)
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
       return context

class SingInvSimpPVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvSimpPV
    template_name = 'tvm_app/SingInvSimp/SingInvSimpPV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvSimpNCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvSimpNModelForm
    template_name = 'tvm_app/SingInvSimp/SingInvSimpN_form.html'
    model = models.SingInvSimpN

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvSimpNDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvSimpN
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvSimp/SingInvSimpN_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvSimpNDetailView, self).get_context_data(**kwargs)
       curr = SingInvSimpN.objects.get(pk=self.object.pk)
       n = int(curr.answer) + 1
       pv = curr.pv
       i = curr.i
       if((n>0) and (pv>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = pv*(1+((i/100)*j))
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
       return context

class SingInvSimpNDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvSimpN
    template_name = 'tvm_app/SingInvSimp/SingInvSimpN_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvSimpICreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvSimpIModelForm
    template_name = 'tvm_app/SingInvSimp/SingInvSimpI_form.html'
    model = models.SingInvSimpI

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvSimpIDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvSimpI
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvSimp/SingInvSimpI_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvSimpIDetailView, self).get_context_data(**kwargs)
       curr = SingInvSimpI.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       pv = curr.pv
       i = curr.answer
       if((n>0) and (pv>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = pv*(1+((i/100)*j))
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
       return context

class SingInvSimpIDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvSimpI
    template_name = 'tvm_app/SingInvSimp/SingInvSimpI_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvCompAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvCompAVModelForm
    template_name = 'tvm_app/SingInvComp/SingInvCompAV_form.html'
    model = models.SingInvCompAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvCompAVDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvCompAV
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvComp/SingInvCompAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvCompAVDetailView, self).get_context_data(**kwargs)
       curr = SingInvCompAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i
       if ((n > 0) and (c > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           	ans = c*((1+(i/100))**j)
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
       return context

class SingInvCompAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvCompAV
    template_name = 'tvm_app/SingInvComp/SingInvCompAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvCompPVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvCompPVModelForm
    template_name = 'tvm_app/SingInvComp/SingInvCompPV_form.html'
    model = models.SingInvCompPV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvCompPVDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvCompPV
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvComp/SingInvCompPV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvCompPVDetailView, self).get_context_data(**kwargs)
       curr = SingInvCompPV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.av
       i = curr.i
       if ((n > 0) and (c > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           	ans = c*((1+(i/100))**(-j))
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
       return context

class SingInvCompPVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvCompPV
    template_name = 'tvm_app/SingInvComp/SingInvCompPV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvCompNCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvCompNModelForm
    template_name = 'tvm_app/SingInvComp/SingInvCompN_form.html'
    model = models.SingInvCompN

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvCompNDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvCompN
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvComp/SingInvCompN_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvCompNDetailView, self).get_context_data(**kwargs)
       curr = SingInvCompN.objects.get(pk=self.object.pk)
       n = int(curr.answer) + 1
       pv = curr.pv
       i = curr.i
       if((n>0) and (pv>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = pv*(1+((i/100)*j))
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
       return context

class SingInvCompNDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvCompN
    template_name = 'tvm_app/SingInvComp/SingInvCompN_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class SingInvCompICreateView(LoginRequiredMixin,CreateView):
    form_class = forms.SingInvCompIModelForm
    template_name = 'tvm_app/SingInvComp/SingInvCompI_form.html'
    model = models.SingInvCompI

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingInvCompIDetailView(LoginRequiredMixin,DetailView):
    model = models.SingInvCompI
    context_object_name = 'detail'
    template_name = 'tvm_app/SingInvComp/SingInvCompI_detail.html'

    def get_context_data(self, **kwargs):
       context = super(SingInvCompIDetailView, self).get_context_data(**kwargs)
       curr = SingInvCompI.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       pv = curr.pv
       i = curr.answer
       if((n>0) and (pv>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = pv*(1+((i/100)*j))
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
       return context

class SingInvCompIDeleteView(LoginRequiredMixin,DeleteView):
    model = models.SingInvCompI
    template_name = 'tvm_app/SingInvComp/SingInvCompI_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuArrAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuArrAVModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrAV_form.html'
    model = models.ConsAnnuArrAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuArrAVDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuArrAV
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuArrAVDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuArrAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuArrAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuArrAV
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuAdvAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuAdvAVModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvAV_form.html'
    model = models.ConsAnnuAdvAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuAdvAVDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuAdvAV
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuAdvAVDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuAdvAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * (1+i) * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuAdvAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuAdvAV
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuPVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuPVModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuPV_form.html'
    model = models.ConsAnnuPV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuPVDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuPV
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuPV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuPVDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuPV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       av = curr.av
       i = curr.i
       if((n>0) and (av>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = av * ((1+(i/100))**(-j))
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
       return context

class ConsAnnuPVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuPV
    template_name = 'tvm_app/ConsAnnu/ConsAnnuPV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class IncAnnuArrAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.IncAnnuArrAVModelForm
    template_name = 'tvm_app/IncAnnu/IncAnnuArrAV_form.html'
    model = models.IncAnnuArrAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IncAnnuArrAVDetailView(LoginRequiredMixin,DetailView):
    model = models.IncAnnuArrAV
    context_object_name = 'detail'
    template_name = 'tvm_app/IncAnnu/IncAnnuArrAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(IncAnnuArrAVDetailView, self).get_context_data(**kwargs)
       curr = IncAnnuArrAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       x = curr.x
       i = curr.i
       j = curr.j
       idi = curr.i/100
       iji = curr.j/100
       ip = 1+(curr.i/100)
       ij = 1+(curr.j/100)
       if((n>0) and (x>0) and (i>0) and (j>0) and (i>j)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for k in range(0,n):
            ans = ((c*(ip**k))+(x*((ip**k)-(ij**k))/(idi-iji)))
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
       return context

class IncAnnuArrAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.IncAnnuArrAV
    template_name = 'tvm_app/IncAnnu/IncAnnuArrAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class IncAnnuAdvAVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.IncAnnuAdvAVModelForm
    template_name = 'tvm_app/IncAnnu/IncAnnuAdvAV_form.html'
    model = models.IncAnnuAdvAV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IncAnnuAdvAVDetailView(LoginRequiredMixin,DetailView):
    model = models.IncAnnuAdvAV
    context_object_name = 'detail'
    template_name = 'tvm_app/IncAnnu/IncAnnuAdvAV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(IncAnnuAdvAVDetailView, self).get_context_data(**kwargs)
       curr = IncAnnuAdvAV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       x = curr.x
       i = curr.i
       j = curr.j
       idi = curr.i/100
       iji = curr.j/100
       ip = 1+(curr.i/100)
       ij = 1+(curr.j/100)
       if((n>0) and (x>0) and (i>0) and (j>0) and (i>j)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for k in range(0,n):
            ans = ((c*(ip**k))+(x*ip*((ip**k)-(ij**k))/(idi-iji)))
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
       return context

class IncAnnuAdvAVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.IncAnnuAdvAV
    template_name = 'tvm_app/IncAnnu/IncAnnuAdvAV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class IncAnnuPVCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.IncAnnuPVModelForm
    template_name = 'tvm_app/IncAnnu/IncAnnuPV_form.html'
    model = models.IncAnnuPV

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class IncAnnuPVDetailView(LoginRequiredMixin,DetailView):
    model = models.IncAnnuPV
    context_object_name = 'detail'
    template_name = 'tvm_app/IncAnnu/IncAnnuPV_detail.html'

    def get_context_data(self, **kwargs):
       context = super(IncAnnuPVDetailView, self).get_context_data(**kwargs)
       curr = IncAnnuPV.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       av = curr.av
       i = curr.i
       if((n>0) and (av>0) and (i>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
       	    l1 = list(t1)
       	    l1.append(j)
       	    t1 = tuple(l1)

       	for j in range(0,n):
       	    ans = av * ((1+(i/100))**(-j))
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
       return context

class IncAnnuPVDeleteView(LoginRequiredMixin,DeleteView):
    model = models.IncAnnuPV
    template_name = 'tvm_app/IncAnnu/IncAnnuPV_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuArrCCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuArrCModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrC_form.html'
    model = models.ConsAnnuArrC

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuArrCDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuArrC
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrC_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuArrCDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuArrC.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.answer
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuArrCDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuArrC
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrC_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuArrXCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuArrXModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrX_form.html'
    model = models.ConsAnnuArrX

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuArrXDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuArrX
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrX_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuArrXDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuArrX.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.answer
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuArrXDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuArrX
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrX_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuArrNCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuArrNModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrN_form.html'
    model = models.ConsAnnuArrN

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuArrNDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuArrN
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrN_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuArrNDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuArrN.objects.get(pk=self.object.pk)
       n = int(curr.answer) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0) and (x>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuArrNDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuArrN
    template_name = 'tvm_app/ConsAnnu/ConsAnnuArrN_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuAdvCCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuAdvCModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvC_form.html'
    model = models.ConsAnnuAdvC

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuAdvCDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuAdvC
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvC_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuAdvCDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuAdvC.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.answer
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x *(1+i) *( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuAdvCDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuAdvC
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvC_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuAdvXCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuAdvXModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvX_form.html'
    model = models.ConsAnnuAdvX

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuAdvXDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuAdvX
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvX_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuAdvXDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuAdvX.objects.get(pk=self.object.pk)
       n = int(curr.n) + 1
       c = curr.c
       i = curr.i/100
       x = curr.answer
       if ((n > 0) and (i > 0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x *(1+i) * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuAdvXDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuAdvX
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvX_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')

class ConsAnnuAdvNCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.ConsAnnuAdvNModelForm
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvN_form.html'
    model = models.ConsAnnuAdvN

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ConsAnnuAdvNDetailView(LoginRequiredMixin,DetailView):
    model = models.ConsAnnuAdvN
    context_object_name = 'detail'
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvN_detail.html'

    def get_context_data(self, **kwargs):
       context = super(ConsAnnuAdvNDetailView, self).get_context_data(**kwargs)
       curr = ConsAnnuAdvN.objects.get(pk=self.object.pk)
       n = int(curr.answer) + 1
       c = curr.c
       i = curr.i/100
       x = curr.x
       if ((n > 0) and (i > 0) and (x>0)):
       	t1 = ()
       	t2 = ()
       	for j in range(0,n):
           	l1 = list(t1)
           	l1.append(j)
           	t1 = tuple(l1)

       	for j in range(0,n):
           ans = (( c* ((1+i)**j) ) + ( x * (1+i) * ( (((1+i)**j)-1)/i) ))
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
       return context

class ConsAnnuAdvNDeleteView(LoginRequiredMixin,DeleteView):
    model = models.ConsAnnuAdvN
    template_name = 'tvm_app/ConsAnnu/ConsAnnuAdvN_delete.html'
    success_url = reverse_lazy('tvm_app:tvm_list')
