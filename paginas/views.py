from django.views.generic import TemplateView
from cadastros.models import Projeto, Tarefa

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        context['qtde_projetos'] = Projeto.objects.all().count()
        
        if(self.request.user.is_authenticated):
            context['m_tarefas'] = Tarefa.objects.count()
            
        context['tarefas'] = Tarefa.objects.all().order_by('nome')
        #context['projeto'] = Projeto.objects.get(pk=1)
                    
        return context
    
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    