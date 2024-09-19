# Lista para armazenar disciplinas
disciplinas = []

# Função para adicionar uma disciplina
def adicionar_disciplina(nome, creditos, data):
    if somar_creditos() + creditos > 28:
        print("Erro: Número máximo de créditos excedido.")
        return False
    disciplina = {"nome": nome, "creditos": creditos, "data": data}
    disciplinas.append(disciplina)
    print("Disciplina adicionada com sucesso!")
    return True

# Função para remover uma disciplina
def remover_disciplina(nome):
    for disciplina in disciplinas:
        if disciplina["nome"] == nome:
            disciplinas.remove(disciplina)
            print("Disciplina removida com sucesso!")
            return True
    print("Erro: Disciplina não encontrada.")
    return False

# Função para atualizar uma disciplina
def atualizar_disciplina(nome, novos_creditos, nova_data):
    for disciplina in disciplinas:
        if disciplina["nome"] == nome:
            disciplina["creditos"] = novos_creditos
            disciplina["data"] = nova_data
            print("Disciplina atualizada com sucesso!")
            return True
    print("Erro: Disciplina não encontrada.")
    return False

# Função para visualizar todas as disciplinas
def visualizar_disciplinas():
    if not disciplinas:
        print("\nNão há disciplinas cadastradas.")
    else:
        total_creditos = somar_creditos()
        print("\nControle Acadêmico - Matrícula:\n")
        for disciplina in disciplinas:
            print(f"- {disciplina['nome']}")
            print(f"    Quantidade de Créditos: {disciplina['creditos']}")
            print(f"    Última alteração em: {disciplina['data']}\n")
        print(f"\nTotal de Créditos: {total_creditos}")
        if 18 <= total_creditos <= 28:
            print("Matrícula aprovada!")
        else:
            print("Matrícula não aprovada! Verifique a quantidade de créditos.")

# Função para somar os créditos
def somar_creditos():
    return sum(disciplina['creditos'] for disciplina in disciplinas)

# Função para filtrar disciplinas
def filtrar_disciplinas(opcao, valor):
    if opcao == 1:  # Filtrar por nome
        disciplinas_filtradas = [disciplina for disciplina in disciplinas if valor.lower() in disciplina["nome"].lower()]
    elif opcao == 2:  # Filtrar por data
        disciplinas_filtradas = [disciplina for disciplina in disciplinas if disciplina["data"] == valor]
    
    if disciplinas_filtradas:
        for disciplina in disciplinas_filtradas:
            print(f"- {disciplina['nome']}")
            print(f"    Quantidade de Créditos: {disciplina['creditos']}")
            print(f"    Última alteração em: {disciplina['data']}")
    else:
        print("Nenhuma disciplina encontrada com esses critérios.")

# Programa principal
def menu():
    while True:
        print("\n1 - Adicionar Disciplina")
        print("2 - Remover Disciplina")
        print("3 - Atualizar Disciplina")
        print("4 - Visualizar Todas as Disciplinas")
        print("5 - Filtrar Disciplinas")
        print("0 - Sair")

        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 1:
            nome = input("Digite o nome da disciplina: ")
            creditos = int(input("Digite a quantidade de créditos: "))
            data = input("Digite a data de cadastro (dd-mm-yyyy): ")
            adicionar_disciplina(nome, creditos, data)
        
        elif opcao == 2:
            nome = input("Digite o nome da disciplina a remover: ")
            remover_disciplina(nome)
        
        elif opcao == 3:
            nome = input("Digite o nome da disciplina a atualizar: ")
            novos_creditos = int(input("Digite a nova quantidade de créditos: "))
            nova_data = input("Digite a nova data de cadastro (dd-mm-yyyy): ")
            atualizar_disciplina(nome, novos_creditos, nova_data)
        
        elif opcao == 4:
            visualizar_disciplinas()
        
        elif opcao == 5:
            print("1 - Filtrar por nome")
            print("2 - Filtrar por data")
            opcao_filtro = int(input("Escolha uma opção: "))
            valor = input("Digite a data desejada: ")
            filtrar_disciplinas(opcao_filtro, valor)

        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

menu()