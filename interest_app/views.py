#FinCalc\interest_app\views.py
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
from .models import AEtoEP, AEtoNP, AEtoC, EPtoAE, EPtoEP, EPtoNP, EPtoC, NPtoAE, NPtoNP, NPtoEP, NPtoC, CtoAE, CtoEP, CtoNP

# Create your views here.

User = get_user_model()
# curr_user = User.username

class InterestHomeView(TemplateView):
    template_name = 'interest_app/interest_index.html'

class InterestCalcView(LoginRequiredMixin,TemplateView):
    template_name = 'interest_app/calc_interest.html'

class InterestListView(LoginRequiredMixin,ListView):
    template_name = 'interest_app/interest_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        queryset = AEtoNP.objects.all()
        #username = request.POST.get('username', None)
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = queryset.filter(user=username).order_by('description')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(InterestListView, self).get_context_data(**kwargs)
        AEtoEP_list = AEtoEP.objects.all()
        AEtoC_list = AEtoC.objects.all()
        EPtoAE_list = EPtoAE.objects.all()
        EPtoEP_list = EPtoEP.objects.all()
        EPtoNP_list = EPtoNP.objects.all()
        EPtoC_list = EPtoC.objects.all()
        NPtoAE_list = NPtoAE.objects.all()
        NPtoNP_list = NPtoNP.objects.all()
        NPtoEP_list = NPtoEP.objects.all()
        NPtoC_list = NPtoC.objects.all()
        CtoAE_list = CtoAE.objects.all()
        CtoEP_list = CtoEP.objects.all()
        CtoNP_list = CtoNP.objects.all()
        #username = request.POST.get('username', None)
        username = User.objects.get(username=self.request.user.username)
        if username is not None:
            AEtoEP_list = AEtoEP_list.filter(user=username).order_by('description')
            AEtoC_list = AEtoC_list.filter(user=username).order_by('description')
            EPtoAE_list = EPtoAE_list.filter(user=username).order_by('description')
            EPtoEP_list = EPtoEP_list.filter(user=username).order_by('description')
            EPtoNP_list = EPtoNP_list.filter(user=username).order_by('description')
            EPtoC_list = EPtoC_list.filter(user=username).order_by('description')
            NPtoAE_list = NPtoAE_list.filter(user=username).order_by('description')
            NPtoNP_list = NPtoNP_list.filter(user=username).order_by('description')
            NPtoEP_list = NPtoEP_list.filter(user=username).order_by('description')
            NPtoC_list = NPtoC_list.filter(user=username).order_by('description')
            CtoAE_list = CtoAE_list.filter(user=username).order_by('description')
            CtoEP_list = CtoEP_list.filter(user=username).order_by('description')
            CtoNP_list = CtoNP_list.filter(user=username).order_by('description')
        context['AEtoEP_list'] = AEtoEP_list
        context['AEtoC_list'] = AEtoC_list
        context['EPtoAE_list'] = EPtoAE_list
        context['EPtoEP_list'] = EPtoEP_list
        context['EPtoNP_list'] = EPtoNP_list
        context['EPtoC_list'] = EPtoC_list
        context['NPtoAE_list'] = NPtoAE_list
        context['NPtoNP_list'] = NPtoNP_list
        context['NPtoEP_list'] = NPtoEP_list
        context['NPtoC_list'] = NPtoC_list
        context['CtoAE_list'] = CtoAE_list
        context['CtoEP_list'] = CtoEP_list
        context['CtoNP_list'] = CtoNP_list
        return context

class AEtoNPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.AEtoNPModelForm
    template_name = 'interest_app/AEtoNP/AEtoNP_form.html'
    model = models.AEtoNP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AEtoNPDetailView(LoginRequiredMixin,DetailView):
    model = models.AEtoNP
    context_object_name = 'detail'
    template_name = 'interest_app/AEtoNP/AEtoNP_detail.html'

class AEtoNPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.AEtoNP
    template_name = 'interest_app/AEtoNP/AEtoNP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class AEtoEPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.AEtoEPModelForm
    template_name = 'interest_app/AEtoEP/AEtoEP_form.html'
    model = models.AEtoEP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AEtoEPDetailView(LoginRequiredMixin,DetailView):
    model = models.AEtoEP
    context_object_name = 'detail'
    template_name = 'interest_app/AEtoEP/AEtoEP_detail.html'

class AEtoEPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.AEtoEP
    template_name = 'interest_app/AEtoEP/AEtoEP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class AEtoCCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.AEtoCModelForm
    template_name = 'interest_app/AEtoC/AEtoC_form.html'
    model = models.AEtoC

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AEtoCDetailView(LoginRequiredMixin,DetailView):
    model = models.AEtoC
    context_object_name = 'detail'
    template_name = 'interest_app/AEtoC/AEtoC_detail.html'

class AEtoCDeleteView(LoginRequiredMixin,DeleteView):
    model = models.AEtoC
    template_name = 'interest_app/AEtoC/AEtoC_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class EPtoAECreateView(LoginRequiredMixin,CreateView):
    form_class = forms.EPtoAEModelForm
    template_name = 'interest_app/EPtoAE/EPtoAE_form.html'
    model = models.EPtoAE

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EPtoAEDetailView(LoginRequiredMixin,DetailView):
    model = models.EPtoAE
    context_object_name = 'detail'
    template_name = 'interest_app/EPtoAE/EPtoAE_detail.html'

class EPtoAEDeleteView(LoginRequiredMixin,DeleteView):
    model = models.EPtoAE
    template_name = 'interest_app/EPtoAE/EPtoAE_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class EPtoEPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.EPtoEPModelForm
    template_name = 'interest_app/EPtoEP/EPtoEP_form.html'
    model = models.EPtoEP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EPtoEPDetailView(LoginRequiredMixin,DetailView):
    model = models.EPtoEP
    context_object_name = 'detail'
    template_name = 'interest_app/EPtoEP/EPtoEP_detail.html'

class EPtoEPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.EPtoEP
    template_name = 'interest_app/EPtoEP/EPtoEP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class EPtoNPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.EPtoNPModelForm
    template_name = 'interest_app/EPtoNP/EPtoNP_form.html'
    model = models.EPtoNP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EPtoNPDetailView(LoginRequiredMixin,DetailView):
    model = models.EPtoNP
    context_object_name = 'detail'
    template_name = 'interest_app/EPtoNP/EPtoNP_detail.html'

class EPtoNPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.EPtoNP
    template_name = 'interest_app/EPtoNP/EPtoNP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class EPtoCCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.EPtoCModelForm
    template_name = 'interest_app/EPtoC/EPtoC_form.html'
    model = models.EPtoC

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EPtoCDetailView(LoginRequiredMixin,DetailView):
    model = models.EPtoC
    context_object_name = 'detail'
    template_name = 'interest_app/EPtoC/EPtoC_detail.html'

class EPtoCDeleteView(LoginRequiredMixin,DeleteView):
    model = models.EPtoC
    template_name = 'interest_app/EPtoC/EPtoC_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class NPtoAECreateView(LoginRequiredMixin,CreateView):
    form_class = forms.NPtoAEModelForm
    template_name = 'interest_app/NPtoAE/NPtoAE_form.html'
    model = models.NPtoAE

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class NPtoAEDetailView(LoginRequiredMixin,DetailView):
    model = models.NPtoAE
    context_object_name = 'detail'
    template_name = 'interest_app/NPtoAE/NPtoAE_detail.html'

class NPtoAEDeleteView(LoginRequiredMixin,DeleteView):
    model = models.NPtoAE
    template_name = 'interest_app/NPtoAE/NPtoAE_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class NPtoNPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.NPtoNPModelForm
    template_name = 'interest_app/NPtoNP/NPtoNP_form.html'
    model = models.NPtoNP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class NPtoNPDetailView(LoginRequiredMixin,DetailView):
    model = models.NPtoNP
    context_object_name = 'detail'
    template_name = 'interest_app/NPtoNP/NPtoNP_detail.html'

class NPtoNPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.NPtoNP
    template_name = 'interest_app/NPtoNP/NPtoNP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class NPtoEPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.NPtoEPModelForm
    template_name = 'interest_app/NPtoEP/NPtoEP_form.html'
    model = models.NPtoEP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class NPtoEPDetailView(LoginRequiredMixin,DetailView):
    model = models.NPtoEP
    context_object_name = 'detail'
    template_name = 'interest_app/NPtoEP/NPtoEP_detail.html'

class NPtoEPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.NPtoEP
    template_name = 'interest_app/NPtoEP/NPtoEP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class NPtoCCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.NPtoCModelForm
    template_name = 'interest_app/NPtoC/NPtoC_form.html'
    model = models.NPtoC

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class NPtoCDetailView(LoginRequiredMixin,DetailView):
    model = models.NPtoC
    context_object_name = 'detail'
    template_name = 'interest_app/NPtoC/NPtoC_detail.html'

class NPtoCDeleteView(LoginRequiredMixin,DeleteView):
    model = models.NPtoC
    template_name = 'interest_app/NPtoC/NPtoC_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class CtoAECreateView(LoginRequiredMixin,CreateView):
    form_class = forms.CtoAEModelForm
    template_name = 'interest_app/CtoAE/CtoAE_form.html'
    model = models.CtoAE

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class CtoAEDetailView(LoginRequiredMixin,DetailView):
    model = models.CtoAE
    context_object_name = 'detail'
    template_name = 'interest_app/CtoAE/CtoAE_detail.html'

class CtoAEDeleteView(LoginRequiredMixin,DeleteView):
    model = models.CtoAE
    template_name = 'interest_app/CtoAE/CtoAE_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class CtoEPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.CtoEPModelForm
    template_name = 'interest_app/CtoEP/CtoEP_form.html'
    model = models.CtoEP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class CtoEPDetailView(LoginRequiredMixin,DetailView):
    model = models.CtoEP
    context_object_name = 'detail'
    template_name = 'interest_app/CtoEP/CtoEP_detail.html'

class CtoEPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.CtoEP
    template_name = 'interest_app/CtoEP/CtoEP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')

class CtoNPCreateView(LoginRequiredMixin,CreateView):
    form_class = forms.CtoNPModelForm
    template_name = 'interest_app/CtoNP/CtoNP_form.html'
    model = models.CtoNP

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class CtoNPDetailView(LoginRequiredMixin,DetailView):
    model = models.CtoNP
    context_object_name = 'detail'
    template_name = 'interest_app/CtoNP/CtoNP_detail.html'

class CtoNPDeleteView(LoginRequiredMixin,DeleteView):
    model = models.CtoNP
    template_name = 'interest_app/CtoNP/CtoNP_delete.html'
    success_url = reverse_lazy('interest_app:interest_list')
