from django.db import models

STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('andamento', 'Andamento'),
    ('concluido', 'Concluido'),
)

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=120, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nome

class Designer(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=120, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='designers/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    designers = models.ManyToManyField(Designer)

    def __str__(self):
        return self.nome

class Feedback(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, blank=True, null=True)
    comentarios = models.TextField()
    data_feedback = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Feedback de {self.cliente} para {self.projeto}"

class Fatura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_emissao = models.DateField()
    data_vencimento = models.DateField()
    status_pagamento = models.CharField(max_length=20)

    def __str__(self):
        return f"Fatura {self.id} - {self.cliente}"
