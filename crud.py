# Lista para armazenar disciplinas
disciplinas = []

# Função para adicionar uma disciplina
def adicionar_disciplina(nome, creditos, data):
    if validar_creditos(creditos):
        if somar_creditos() + creditos > 28:
            print("\nErro: Número máximo de créditos excedido.")
            return False
        disciplina = {"nome": nome, "creditos": creditos, "data": data}
        disciplinas.append(disciplina)
        print("\nDisciplina adicionada com sucesso!")
        return True
    print("\nErro: Quantidade de Créditos inválida.")
    return False

# Função para remover uma disciplina
def remover_disciplina(nome):
    for disciplina in disciplinas:
        if disciplina["nome"] == nome:
            disciplinas.remove(disciplina)
            print("\nDisciplina removida com sucesso!")
            return True
    print("\nErro: Disciplina não encontrada.")
    return False

# Função para atualizar uma disciplina
def atualizar_disciplina(nome, novos_creditos, nova_data):
    for disciplina in disciplinas:
        if disciplina["nome"] == nome:
            disciplina["creditos"] = novos_creditos
            disciplina["data"] = nova_data
            print("\nDisciplina atualizada com sucesso!")
            return True
    print("\nErro: Disciplina não encontrada.")
    return False

# Função para visualizar todas as disciplinas
def visualizar_disciplinas():
    if not disciplinas:
        print("\nNão há disciplinas cadastradas.")
        return False
    total_creditos = somar_creditos()
    print("\nControle Acadêmico - Matrícula:\n")
    for disciplina in disciplinas:
        print(f"- {disciplina['nome']}")
        print(f"    Quantidade de Créditos: {disciplina['creditos']}")
        print(f"    Última alteração em: {disciplina['data']}\n")
    print(f"Total de Créditos: {total_creditos}")
    if 18 <= total_creditos <= 28:
        print("Matrícula aprovada!")
    else:
        print("Matrícula não aprovada! Verifique a quantidade de créditos.")
    return True

# funcao para validar créditos negativos
def validar_creditos(creditos):
    if creditos < 0:
        return False
    return True

# Função para filtrar disciplinas
def filtrar_disciplinas(opcao, valor):
  
    if opcao == 1:  # Filtrar por nome
        disciplinas_filtradas = [disciplina for disciplina in disciplinas if valor.lower() in disciplina["nome"].lower()]
        print("\nDisciplina " + valor + " com última alteração em:")
        for disciplina in disciplinas_filtradas:
            print(f"\n- {disciplina['nome']}")
            print(f"    Quantidade de Créditos: {disciplina['creditos']}")
            print(f"    Última alteração em: {disciplina['data']}")
    elif opcao == 2:  # Filtrar por data
        disciplinas_filtradas = [disciplina for disciplina in disciplinas if disciplina["data"] == valor]
        print("\nDisciplinas com última alteração em " + valor + ":")
        for disciplina in disciplinas_filtradas:
            print(f"\n- {disciplina['nome']}")
            print(f"    Quantidade de Créditos: {disciplina['creditos']}")
            print(f"    Última alteração em: {disciplina['data']}")
    else:
        print("\nNenhuma disciplina encontrada com esses critérios.")

# Função para somar os créditos
def somar_creditos():
    return sum(disciplina['creditos'] for disciplina in disciplinas)

def validar_opcao_menu(opcao):
    if opcao.isdigit() and int(opcao) in [0, 1, 2, 3, 4, 5]:
        return int(opcao)
    return None

def opcao_menu():
    print("\n1 - Adicionar Disciplina")
    print("2 - Remover Disciplina")
    print("3 - Atualizar Disciplina")
    print("4 - Visualizar Todas as Disciplinas")
    print("5 - Filtrar Disciplinas")
    print("0 - Sair")    

# Programa principal
def app():
    while True:
        opcao_menu()

        opcao = input("\nEscolha uma opção: ").strip()
        opcao_valida = validar_opcao_menu(opcao)
        
        if opcao_valida == 1:
            nome = input("\nDigite o nome da disciplina: ")
            creditos = int(input("Digite a quantidade de créditos: "))
            data = input("Digite a data de cadastro: ")
            adicionar_disciplina(nome, creditos, data)
        
        elif opcao_valida == 2:
            if not disciplinas:
                print("\nNão há disciplinas cadastradas.")
            else:
                nome = input("\nDigite o nome da disciplina a remover: ")
                remover_disciplina(nome)
        
        elif opcao_valida == 3:
            if not disciplinas:
                print("\nNão há disciplinas cadastradas.")
            else:
                nome = input("\nDigite o nome da disciplina a atualizar: ")
                novos_creditos = int(input("Digite a nova quantidade de créditos: "))
                nova_data = input("Digite a nova data de cadastro (dd-mm-yyyy): ")
                atualizar_disciplina(nome, novos_creditos, nova_data)
        
        elif opcao_valida == 4:
            visualizar_disciplinas()
        
        elif opcao_valida == 5:
            if not disciplinas:
                print("\nNão há disciplinas cadastradas.")
            else:
                print("1 - Filtrar por nome")
                print("2 - Filtrar por data\n")
                opcao_filtro = int(input("Escolha uma opção: "))
                if opcao_filtro == 1:
                    valor = input("Digite a disciplina desejada: ")
                else: 
                    valor = input("Digite a data desejada: ")
                filtrar_disciplinas(opcao_filtro, valor)

        elif opcao_valida == 0:
            print("Saindo...")
            break
        
        else:
            print("\nOpção inválida, tente novamente.")

app()