import pkgutil
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, response
from django.urls import path
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import (
    Clientes,
    Tratamento,
    Exames
)
from .forms import (
    ClientesModelForm,
    TratamentoModelForm,
    ExameModelForm,
)
from pathlib import Path
from django.conf import settings
import os
from .filters import ClienteFilter


# Views genéricas

class MainPage(LoginRequiredMixin, generic.TemplateView):
    template_name = "main_page.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, "main_page.html")   #redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, "landing.html")   #redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


# Views de gestão de clientes
    
class Clientes_Lista(LoginRequiredMixin, generic.ListView):
    # paginate_by = 3
    model = Clientes

    def get_queryset(self):
        qs = self.model.objects.all()
        cliente_filtered_list = ClienteFilter(self.request.GET, queryset=qs)
        return cliente_filtered_list.qs
 
class Clientes_criar(LoginRequiredMixin, generic.CreateView):
    model = Clientes
    template_name = "clientes/clientes_create.html"
    form_class = ClientesModelForm

    def get_success_url(self):
        return reverse("clientes:clientes-lista")

    def form_valid(self, form):
        clientes = form.save(commit=False)
        clientes.save()
        
        return super(Clientes_criar, self).form_valid(form)

class ClienteUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Clientes
    form_class = ClientesModelForm
    
    def get_success_url(self):
        return reverse("clientes:clientes-detail", args=[self.object.id])

@login_required    
def ClienteDetalhe(request, pk):
    cliente = Clientes.objects.get(id=pk)
    tratamentos = cliente.tratamento_set.all()#[:5]
    exames = cliente.exames_set.all()
    context = {
        'cliente': cliente,
        'tratamentos': tratamentos,
        'exames': exames
    }

    return render(request, 'clientes/clientes_detail.html', context)


# Views de Gestão de Tratamentos

@login_required
def TratamentoLista(request, pk):
    cliente = Clientes.objects.get(id=pk)
    tratamento = cliente.tratamento_set.all()
    context = {
        'cliente': cliente,
        'tratamento': tratamento
        }
    
    return render(request, 'tratamento/tratamento_list.html', context) 

class Tratamento_criar(LoginRequiredMixin, generic.CreateView):
    model = Tratamento
    template_name = "tratamento/tratamento_create.html"
    form_class = TratamentoModelForm

    def get_initial(self):
        initial_data = super(Tratamento_criar, self).get_initial()
        cliente = Clientes.objects.get(id=self.kwargs["pk"])
        initial_data["cliente"] = cliente
        return initial_data

    def get_context_data(self):
        context = super(Tratamento_criar, self).get_context_data()
        cliente = Clientes.objects.get(id=self.kwargs["pk"])
        context["cliente"] = cliente
        return context

    def get_success_url(self):
        return reverse("clientes:clientes-detail", args=[self.object.cliente_id])

class TratamentoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Tratamento
    form_class = TratamentoModelForm
    template_name = "tratamento/tratamento_form.html"


    def get_success_url(self):
        return reverse("clientes:clientes-detail", args=[self.object.cliente_id])


# Views de Gestão de Exames

class Exame_criar(LoginRequiredMixin, generic.CreateView):
    model = Exames
    template_name = "exames/exame_create.html"
    form_class = ExameModelForm

    def get_initial(self):
        initial_data = super(Exame_criar, self).get_initial()
        cliente = Clientes.objects.get(id=self.kwargs["pk"])
        initial_data["cliente"] = cliente
        return initial_data

    def get_context_data(self):
        context = super(Exame_criar, self).get_context_data()
        cliente = Clientes.objects.get(id=self.kwargs["pk"])
        context["cliente"] = cliente
        return context

    def get_success_url(self):
        return reverse("clientes:clientes-detail", args=[self.object.cliente_id])

@login_required
def Exame_view(request,pk):
    exame = Exames.objects.get(id=pk)
    filepath = os.path.join(settings.MEDIA_ROOT, str(exame.Ficheiro))
    ext = os.path.splitext(filepath)[1][1:]
    if ext == 'pdf':
        with open(filepath, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filepath'
            return response
    else:
        filepath = os.path.join(settings.MEDIA_ROOT, str(exame.Ficheiro))
        response = { 'exame': exame.Ficheiro}
        print(response)
        return render(request, 'exames/exame_view.html', response)

class ExameUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Exames
    form_class = ExameModelForm
    template_name = "exames/exame_form.html"


    def get_success_url(self):
        return reverse("clientes:clientes-detail", args=[self.object.cliente_id])