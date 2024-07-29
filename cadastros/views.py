from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Cliente, Designer, Projeto, Tarefa, Feedback, Fatura

# Cliente Views
class ClienteCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco', 'empresa']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Cliente'
        return dados

class ClienteUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco', 'empresa']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Cliente'
        return dados

class ClienteDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cliente')
    model = Cliente

class ClienteList(ListView):
    template_name = 'cadastros/list/cliente.html'
    model = Cliente

# Designer Views
class DesignerCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-designer')
    model = Designer
    fields = ['nome', 'email', 'telefone', 'cargo', 'foto']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Designer'
        return dados

class DesignerUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-designer')
    model = Designer
    fields = ['nome', 'email', 'telefone', 'cargo', 'foto']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Designer'
        return dados

class DesignerDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-designer')
    model = Designer

class DesignerList(ListView):
    template_name = 'cadastros/list/designer.html'
    model = Designer

# Projeto Views
class ProjetoCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-projeto')
    model = Projeto
    fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'status', 'cliente']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Projeto'
        return dados

class ProjetoUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-projeto')
    model = Projeto
    fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'status', 'cliente']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Projeto'
        return dados

class ProjetoDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-projeto')
    model = Projeto

class ProjetoList(ListView):
    template_name = 'cadastros/list/projeto.html'
    model = Projeto

# Tarefa Views
class TarefaCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tarefa')
    model = Tarefa
    fields = ['nome', 'descricao', 'data_conclusao', 'status', 'projeto', 'designers']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Tarefa'
        return dados

class TarefaUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tarefa')
    model = Tarefa
    fields = ['nome', 'descricao', 'data_conclusao', 'status', 'projeto', 'designers']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Tarefa'
        return dados

class TarefaDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tarefa')
    model = Tarefa

class TarefaList(ListView):
    template_name = 'cadastros/list/tarefa.html'
    model = Tarefa

# Feedback Views
class FeedbackCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-feedback')
    model = Feedback
    fields = ['cliente', 'projeto', 'tarefa', 'comentarios']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Feedback'
        return dados

class FeedbackUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-feedback')
    model = Feedback
    fields = ['cliente', 'projeto', 'tarefa', 'comentarios']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Feedback'
        return dados

class FeedbackDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-feedback')
    model = Feedback

class FeedbackList(ListView):
    template_name = 'cadastros/list/feedback.html'
    model = Feedback

# Fatura Views
class FaturaCreate(CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fatura')
    model = Fatura
    fields = ['cliente', 'projeto', 'valor_total', 'data_emissao', 'data_vencimento', 'status_pagamento']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Fatura'
        return dados

class FaturaUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fatura')
    model = Fatura
    fields = ['cliente', 'projeto', 'valor_total', 'data_emissao', 'data_vencimento', 'status_pagamento']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar Fatura'
        return dados

class FaturaDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fatura')
    model = Fatura

class FaturaList(ListView):
    template_name = 'cadastros/list/fatura.html'
    model = Fatura
