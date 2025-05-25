# test_todo_cli.py
import pytest
from todo_cli import Tarefa, GerenciadorTarefas

# --- Testes para a classe Tarefa ---
def test_criar_tarefa_com_descricao():
    tarefa = Tarefa("Lavar louça")
    assert tarefa.descricao == "Lavar louça"
    assert not tarefa.concluida

def test_criar_tarefa_sem_descricao_deve_lancar_erro():
    with pytest.raises(ValueError) as excinfo:
        Tarefa("")
    assert "descrição da tarefa não pode ser vazia" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo_none:
        Tarefa(None) # type: ignore
    assert "descrição da tarefa não pode ser vazia" in str(excinfo_none.value)

def test_marcar_tarefa_como_concluida():
    tarefa = Tarefa("Estudar Pytest")
    tarefa.marcar_como_concluida()
    assert tarefa.concluida

def test_representacao_string_tarefa():
    tarefa_pendente = Tarefa("Comprar pão")
    assert str(tarefa_pendente) == "Comprar pão [Pendente]"
    tarefa_concluida = Tarefa("Fazer café")
    tarefa_concluida.marcar_como_concluida()
    assert str(tarefa_concluida) == "Fazer café [Concluída]"

def test_marcar_tarefa_pendente():
    tarefa = Tarefa("Lavar Louça")
    tarefa.marcar_como_concluida()
    tarefa.marcar_como_pendente()
    
    assert tarefa.concluida == False

# --- Testes para a classe GerenciadorTarefas ---
@pytest.fixture
def gerenciador():
    return GerenciadorTarefas()

def test_adicionar_tarefa_sucesso(gerenciador):
    assert gerenciador.adicionar_tarefa("Nova Tarefa Teste")
    pendentes = gerenciador.get_tarefas_pendentes()
    assert len(pendentes) == 1
    assert pendentes[0][1] == "Nova Tarefa Teste [Pendente]"

def test_adicionar_tarefa_descricao_invalida(gerenciador):
    assert not gerenciador.adicionar_tarefa("") # Descrição vazia
    pendentes = gerenciador.get_tarefas_pendentes()
    assert len(pendentes) == 0

def test_listar_tarefas_vazias(gerenciador):
    assert gerenciador.get_tarefas_pendentes() == []
    assert gerenciador.get_tarefas_concluidas() == []
    assert gerenciador.listar_tarefas() == []

def test_marcar_tarefa_como_concluida_sucesso(gerenciador):
    gerenciador.adicionar_tarefa("Tarefa para concluir")
    # As tarefas são listadas com índice 1-based para o usuário
    assert gerenciador.marcar_como_concluida("1")
    concluidas = gerenciador.get_tarefas_concluidas()
    assert len(concluidas) == 1
    assert concluidas[0][1] == "Tarefa para concluir [Concluída]"
    assert len(gerenciador.get_tarefas_pendentes()) == 0

def test_marcar_tarefa_como_concluida_indice_invalido(gerenciador):
    gerenciador.adicionar_tarefa("Tarefa X")
    assert not gerenciador.marcar_como_concluida("2") # Índice não existe
    assert not gerenciador.marcar_como_concluida("abc") # Índice não numérico
    assert not gerenciador.marcar_como_concluida("0") # Índice 0 (usuário usa 1-based)

def test_marcar_tarefa_ja_concluida(gerenciador):
    gerenciador.adicionar_tarefa("Tarefa Y")
    gerenciador.marcar_como_concluida("1") # Marca pela primeira vez
    assert not gerenciador.marcar_como_concluida("1") # Tenta marcar novamente

def test_remover_tarefa_sucesso(gerenciador):
    gerenciador.adicionar_tarefa("Tarefa A")
    gerenciador.adicionar_tarefa("Tarefa B")
    assert gerenciador.remover_tarefa("1") # Remove "Tarefa A"
    pendentes = gerenciador.get_tarefas_pendentes()
    assert len(pendentes) == 1
    assert pendentes[0][1] == "Tarefa B [Pendente]" # "Tarefa B" agora é a primeira

def test_remover_tarefa_indice_invalido(gerenciador):
    gerenciador.adicionar_tarefa("Tarefa Z")
    assert not gerenciador.remover_tarefa("2")
    assert not gerenciador.remover_tarefa("abc")
    pendentes = gerenciador.get_tarefas_pendentes()
    assert len(pendentes) == 1 # Nenhuma tarefa deve ter sido removida

def test_listar_tarefas_pendentes_e_concluidas_separadamente(gerenciador):
    gerenciador.adicionar_tarefa("Pendente 1")
    gerenciador.adicionar_tarefa("Para Concluir 1")
    gerenciador.adicionar_tarefa("Pendente 2")

    gerenciador.marcar_como_concluida("2") # Marca "Para Concluir 1"

    pendentes = gerenciador.get_tarefas_pendentes()
    concluidas = gerenciador.get_tarefas_concluidas()

    assert len(pendentes) == 2
    # Verifica se as descrições das pendentes estão corretas, ignorando o índice exato
    descricoes_pendentes = [p[1] for p in pendentes]
    assert "Pendente 1 [Pendente]" in descricoes_pendentes
    assert "Pendente 2 [Pendente]" in descricoes_pendentes

    assert len(concluidas) == 1
    assert concluidas[0][1] == "Para Concluir 1 [Concluída]"

def test_listar_todas_tarefas_sem_filtro(gerenciador):
    gerenciador.adicionar_tarefa("Pendente 1")
    gerenciador.adicionar_tarefa("Para Concluir 1")
    gerenciador.adicionar_tarefa("Pendente 2")

    gerenciador.marcar_como_concluida("2")
    
    tarefas = gerenciador.listar_tarefas()
    
    assert len(tarefas) == 3
    descricoes = [t[1] for t in tarefas]
    assert "Pendente 1 [Pendente]" in descricoes
    assert "Para Concluir 1 [Concluída]" in descricoes
    assert "Pendente 2 [Pendente]" in descricoes

# Adicione mais testes:
# - Testar a remoção de uma tarefa e como isso afeta os índices das demais.
# - Testar o comportamento quando a lista está vazia para todas as operações.