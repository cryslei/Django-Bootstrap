from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import *
from .forms import *
from django.views.generic import FormView

class RelatorioList(FormView):
    model = Relatorio  
    template_name = "sistema/pesquisa.html"
    form_class = RelatorioForm

    def form_valid(self, form):
        dados = form.clean()
        add = Relatorio(
            patrimonio=dados['patrimonio'], estado=dados['estado'], nome=dados['nome'], serie=dados['serie'], marca=dados['marca'], setor=dados['setor'], data_saida=dados['data_saida'], data_retorno=dados['data_retorno'], descricao=dados['descricao'])
        add.save()
        return super().form_valid(form)
        
def relatorio_geral(request):
    relatorio = Relatorio.objects.all()
    return render(request,'sistema/relatorio.html',{'relatorio':relatorio})

def relatorio(request,relatorio_id):
    try:
        relatorio = Relatorio.objects.get(pk=relatorio_id)
        #relatorio = Relatorio.objects.filter(patrimonio=patrimonio)
    except Relatorio.DoesNotExist:
        raise Http404('Relatorio não encontrado')
    return render(request , 'sistema/modelo.html', {'relatorio':relatorio})
def home(request):
    return render(request,'sistema/index.html')
def redirect(request):
    return HttpResponseRedirect ('home/')