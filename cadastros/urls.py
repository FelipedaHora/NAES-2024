from django.urls import path
from .views import (
    ClienteCreate, ClienteUpdate, ClienteDelete, ClienteList,
    DesignerCreate, DesignerUpdate, DesignerDelete, DesignerList,
    ProjetoCreate, ProjetoUpdate, ProjetoDelete, ProjetoList,
    TarefaCreate, TarefaUpdate, TarefaDelete, TarefaList,
    FeedbackCreate, FeedbackUpdate, FeedbackDelete, FeedbackList,
    FaturaCreate, FaturaUpdate, FaturaDelete, FaturaList
)

urlpatterns = [
    # URLs para Cliente
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
    path('listar/clientes/', ClienteList.as_view(), name='listar-cliente'),

    # URLs para Designer
    path('cadastrar/designer/', DesignerCreate.as_view(), name='cadastrar-designer'),
    path('editar/designer/<int:pk>/', DesignerUpdate.as_view(), name='editar-designer'),
    path('excluir/designer/<int:pk>/', DesignerDelete.as_view(), name='excluir-designer'),
    path('listar/designers/', DesignerList.as_view(), name='listar-designer'),

    # URLs para Projeto
    path('cadastrar/projeto/', ProjetoCreate.as_view(), name='cadastrar-projeto'),
    path('editar/projeto/<int:pk>/', ProjetoUpdate.as_view(), name='editar-projeto'),
    path('excluir/projeto/<int:pk>/', ProjetoDelete.as_view(), name='excluir-projeto'),
    path('listar/projetos/', ProjetoList.as_view(), name='listar-projeto'),

    # URLs para Tarefa
    path('cadastrar/tarefa/', TarefaCreate.as_view(), name='cadastrar-tarefa'),
    path('editar/tarefa/<int:pk>/', TarefaUpdate.as_view(), name='editar-tarefa'),
    path('excluir/tarefa/<int:pk>/', TarefaDelete.as_view(), name='excluir-tarefa'),
    path('listar/tarefas/', TarefaList.as_view(), name='listar-tarefa'),

    # URLs para Feedback
    path('cadastrar/feedback/', FeedbackCreate.as_view(), name='cadastrar-feedback'),
    path('editar/feedback/<int:pk>/', FeedbackUpdate.as_view(), name='editar-feedback'),
    path('excluir/feedback/<int:pk>/', FeedbackDelete.as_view(), name='excluir-feedback'),
    path('listar/feedbacks/', FeedbackList.as_view(), name='listar-feedback'),

    # URLs para Fatura
    path('cadastrar/fatura/', FaturaCreate.as_view(), name='cadastrar-fatura'),
    path('editar/fatura/<int:pk>/', FaturaUpdate.as_view(), name='editar-fatura'),
    path('excluir/fatura/<int:pk>/', FaturaDelete.as_view(), name='excluir-fatura'),
    path('listar/faturas/', FaturaList.as_view(), name='listar-fatura'),
]
