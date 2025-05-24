# Demo-Coverage 🧪📊

Este projeto foi desenvolvido para a disciplina de Teste de Software, com o objetivo de demonstrar a aplicação prática de testes unitários utilizando a biblioteca `pytest` e a análise de cobertura de testes com `coverage.py`. A aplicação base para esta demonstração é um simples Gerenciador de Tarefas (To-Do List) via Interface de Linha de Comando (CLI).

---

## 1. O que é o Projeto?

O **Demo-Coverage** é uma aplicação CLI de Gerenciador de Tarefas desenvolvida em Python. Seu propósito principal não é ser uma ferramenta de produtividade completa, mas sim servir como um estudo de caso para:

- Implementar testes unitários de forma eficaz utilizando `pytest`.
- Identificar as partes do código que foram exercitadas pelos testes.
- Gerar e analisar relatórios de cobertura de teste utilizando a ferramenta `coverage.py`.
- Compreender a importância da cobertura de testes como uma métrica (embora não a única) da qualidade e da robustez dos testes de software.

---

## 2. Funcionalidades da Aplicação (Gerenciador de Tarefas CLI)

O Gerenciador de Tarefas CLI permite ao usuário realizar as seguintes operações:

- **Adicionar Tarefa:** Permite ao usuário inserir novas tarefas na lista.
- **Listar Tarefas Pendentes:** Exibe todas as tarefas que ainda não foram marcadas como concluídas.
- **Listar Tarefas Concluídas:** Exibe todas as tarefas que já foram marcadas como concluídas.
- **Marcar Tarefa como Concluída:** Permite ao usuário selecionar uma tarefa pendente e marcá-la como concluída.
- **Remover Tarefa:** Permite ao usuário remover uma tarefa existente da lista (seja ela pendente ou concluída).

---

## 3. Como Rodar o Projeto e os Testes

Siga os passos abaixo para configurar o ambiente, executar a aplicação e os testes.

### Pré-requisitos

- **Python 3.7+** instalado.

### Configuração do Ambiente

1.  **Clone o repositório** (ou crie os arquivos `todo_cli.py` e `test_todo_cli.py` no seu diretório de projeto).

    ```bash
    # Se você tiver um repositório git
    # git clone <url_do_seu_repositorio>
    # cd Demo-Coverage
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):

    - No Windows (PowerShell):
      ```powershell
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Instale as dependências** (`pytest` e `coverage`):
    ```bash
    pip install pytest coverage
    ```

### Rodando a Aplicação CLI

Com o ambiente virtual ativado e as dependências instaladas, você pode executar o gerenciador de tarefas:

```bash
python todo_cli.py
```
