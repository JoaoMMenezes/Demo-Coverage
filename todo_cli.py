class Tarefa:
    def __init__(self, descricao):
        if not descricao or not isinstance(descricao, str):
            raise ValueError("A descrição da tarefa não pode ser vazia e deve ser uma string.")
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.descricao} [{status}]"

    def marcar_como_concluida(self):
        self.concluida = True

    def marcar_como_pendente(self): # Adicional, pode ser útil
        self.concluida = False


class GerenciadorTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar_tarefa(self, descricao_tarefa):
        """Adiciona uma nova tarefa à lista."""
        try:
            tarefa = Tarefa(descricao_tarefa)
            self._tarefas.append(tarefa)
            return True
        except ValueError:
            return False # Falha ao criar a tarefa (descrição inválida)

    def _encontrar_tarefa_por_indice(self, indice_usuario):
        """
        Converte o índice fornecido pelo usuário (1-based) para o índice da lista (0-based)
        e retorna a tarefa se válida.
        """
        try:
            indice_lista = int(indice_usuario) - 1
            if 0 <= indice_lista < len(self._tarefas):
                return self._tarefas[indice_lista]
            return None
        except ValueError: # Se o índice não for um número
            return None

    def remover_tarefa(self, indice_usuario):
        """Remove uma tarefa com base no seu índice (1-based) na lista completa."""
        try:
            indice_lista = int(indice_usuario) - 1
            if 0 <= indice_lista < len(self._tarefas):
                del self._tarefas[indice_lista]
                return True
            return False # Índice fora do alcance
        except ValueError:
            return False # Índice não é um número

    def marcar_como_concluida(self, indice_usuario):
        """Marca uma tarefa como concluída com base no seu índice (1-based) na lista completa."""
        tarefa = self._encontrar_tarefa_por_indice(indice_usuario)
        if tarefa and not tarefa.concluida:
            tarefa.marcar_como_concluida()
            return True
        return False # Tarefa não encontrada ou já concluída

    def listar_tarefas(self, status_filtro=None):
        """
        Lista tarefas.
        status_filtro: None (todas), True (concluídas), False (pendentes).
        Retorna uma lista de tuplas (índice_usuario, descrição_com_status).
        """
        tarefas_filtradas = []
        for i, tarefa in enumerate(self._tarefas):
            if status_filtro is None or tarefa.concluida == status_filtro:
                tarefas_filtradas.append((i + 1, str(tarefa)))
        return tarefas_filtradas

    def get_tarefas_pendentes(self):
        """Retorna uma lista de tuplas (índice_global, descrição) para tarefas pendentes."""
        pendentes = []
        for i, tarefa in enumerate(self._tarefas):
            if not tarefa.concluida:
                pendentes.append((i + 1, str(tarefa)))
        return pendentes

    def get_tarefas_concluidas(self):
        """Retorna uma lista de tuplas (índice_global, descrição) para tarefas concluídas."""
        concluidas = []
        for i, tarefa in enumerate(self._tarefas):
            if tarefa.concluida:
                concluidas.append((i + 1, str(tarefa)))
        return concluidas

# --- Interface CLI ---
def exibir_menu():
    print("\n--- Gerenciador de Tarefas CLI ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas Pendentes")
    print("3. Listar Tarefas Concluídas")
    print("4. Marcar Tarefa como Concluída")
    print("5. Remover Tarefa")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            if not descricao.strip():
                print("Erro: A descrição não pode ser vazia.")
            elif gerenciador.adicionar_tarefa(descricao):
                print("Tarefa adicionada com sucesso!")
            else:
                print("Erro ao adicionar tarefa (verifique a descrição).")

        elif escolha == '2':
            print("\n--- Tarefas Pendentes ---")
            pendentes = gerenciador.get_tarefas_pendentes()
            if not pendentes:
                print("Nenhuma tarefa pendente.")
            else:
                for idx, desc in pendentes:
                    print(f"{idx}. {desc}")

        elif escolha == '3':
            print("\n--- Tarefas Concluídas ---")
            concluidas = gerenciador.get_tarefas_concluidas()
            if not concluidas:
                print("Nenhuma tarefa concluída.")
            else:
                for idx, desc in concluidas:
                    print(f"{idx}. {desc}")

        elif escolha == '4':
            print("\n--- Marcar Tarefa como Concluída ---")
            pendentes = gerenciador.get_tarefas_pendentes()
            if not pendentes:
                print("Nenhuma tarefa pendente para marcar.")
            else:
                print("Tarefas Pendentes disponíveis para marcar:")
                for idx, desc in pendentes:
                    print(f"{idx}. {desc}")
                try:
                    indice_str = input("Digite o número da tarefa a marcar como concluída: ")
                    if gerenciador.marcar_como_concluida(indice_str):
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Erro: Tarefa não encontrada, já concluída ou índice inválido.")
                except ValueError:
                    print("Erro: Índice inválido.")


        elif escolha == '5':
            print("\n--- Remover Tarefa ---")
            todas_as_tarefas = gerenciador.listar_tarefas() # Lista todas para facilitar a remoção
            if not todas_as_tarefas:
                print("Nenhuma tarefa para remover.")
            else:
                print("Tarefas disponíveis para remover:")
                for idx, desc in todas_as_tarefas:
                    print(f"{idx}. {desc}")
                try:
                    indice_str = input("Digite o número da tarefa a remover: ")
                    if gerenciador.remover_tarefa(indice_str):
                        print("Tarefa removida com sucesso!")
                    else:
                        print("Erro: Tarefa não encontrada ou índice inválido.")
                except ValueError:
                    print("Erro: Índice inválido.")

        elif escolha == '6':
            print("Saindo do gerenciador de tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()