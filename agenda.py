def carregar():  ## Definida a função para carregar o arquivo de texto que funciona  como banco de dados
    agenda = []
    try:
        arquivo = open('agenda.txt', 'r')
        for lin in arquivo.readlines():
            col = lin.strip().split("#")
            contato = {
                'nome': col[0],
                'email': col[1],
                'tel': col[2]
            }
            agenda.append(contato)

        arquivo.close()
    except FileNotFoundError:  #Caso não tenha o arquivo ele inicia ainda
        pass
    return agenda

def salvar(agenda): ## Função para escrever as informações e salvar no arquivo
    arquivo = open('agenda.txt', 'w')

    for contato in agenda:
        arquivo.write("{}#{}#{}\n".format(contato['nome'], contato['email'], contato['tel']))

    arquivo.close()

def incluir(agenda): ## Inclusão de novos contatos
    print("Incluir novo contato")

    contato = {
        'nome': input("Digite o nome: "),
        'email': input("Digite o email: "),
        'tel': input("Digite o telefone: ")
    }
    agenda.append(contato)

def buscar(agenda): ## Busca de contatos
    print("Buscar contato")
    print("Deseja buscar por:")
    print("1 - Nome")
    print("2 - E-mail")  #A busca pode ser filtrada por nome, email e telefone
    print("3 - Telefone")
    buscar = int(input("Insira a opção: "))
    if 0 < buscar < 4:
        if buscar == 1:
            busca = input("insira o nome referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            print("Nome\tE-mail\tTelefone")
            for contato in agenda:
                if busca == contato['nome']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))

        elif buscar == 2:
            busca = input("insira o e-mail referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            for contato in agenda:
                if busca == contato['email']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))

        elif buscar == 3:
            busca = input("insira o telefone referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            for contato in agenda:
                if busca == contato['tel']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))

        elif busca == 0:
            print("saindo...")
def editar(agenda): ## Edição de contatos
    print("Editar contato")
    print("Deseja buscar o contato que será alterado por:")
    print("1 - Nome")
    print("2 - E-mail")  ## A edição pode ser feita por nome, email ou telefone
    print("3 - Telefone")
    buscar = int(input("Insira a opção: "))
    if 0 < buscar < 4:
        if buscar == 1:
            busca = input("insira o nome referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            print("Nome\tE-mail\tTelefone")
            for contato in agenda:
                if busca == contato['nome']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    print("Qual dado deseja alterar:")
                    print("1 - Nome")
                    print("2 - E-mail")  ## Escolha o que irá editar
                    print("3 - Telefone")
                    print("4 - Sair")
                    alt = int(input(">"))
                    if alt == 1:
                        contato['nome'] = input("Digite o novo nome para o usuário: ")

                    elif alt == 2:
                        contato['email'] = input("Digite o novo e-mail para o usuário: ")

                    elif alt == 3:
                        contato['tel'] = input("Digite o novo telefone para o usuário: ")

        elif buscar == 2:
            busca = input("insira o e-mail referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            for contato in agenda:
                if busca == contato['email']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    print("Qual dado deseja alterar:")
                    print("1 - Nome")
                    print("2 - E-mail")
                    print("3 - Telefone")
                    print("4 - Sair")
                    alt = int(input(">"))
                    if alt == 1:
                        contato['nome'] = input("Digite o novo nome para o usuário: ")

                    elif alt == 2:
                        contato['email'] = input("Digite o novo e-mail para o usuário: ")

                    elif alt == 3:
                        contato['tel'] = input("Digite o novo telefone para o usuário: ")

        elif buscar == 3:
            busca = input("insira o telefone referente ao contato que deseja buscar ou digite 0 para cancelar: ")
            for contato in agenda:
                if busca == contato['tel']:
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    print("Qual dado deseja alterar:")
                    print("1 - Nome")
                    print("2 - E-mail")
                    print("3 - Telefone")
                    print("4 - Sair")
                    alt = int(input(">"))
                    if alt == 1:
                        contato['nome'] = input("Digite o novo nome para o usuário: ")

                    elif alt == 2:
                        contato['email'] = input("Digite o novo e-mail para o usuário: ")

                    elif alt == 3:
                        contato['tel'] = input("Digite o novo telefone para o usuário: ")


        elif busca == 0:
            print("saindo...")
    print("Contato alterado")
def excluir(agenda): ## Exclusão de contatos
    print("Excluir contato")
    print("Deseja excluir por:")
    print("1 - Nome")
    print("2 - E-mail")
    print("3 - Telefone")
    buscar = int(input("Insira a opção: "))
    if 0 < buscar < 4:
        if buscar == 1:
            busca = input("insira o nome referente ao contato que deseja excluir ou digite 0 para cancelar: ")
            print("Nome\tE-mail\tTelefone")
            for i, contato in enumerate(agenda):
                if busca == contato['nome']:
                    print("Tem certeza que deseja excluir o seguinte contato? S/N")
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    ex = input(">")
                    if ex == 'S':
                        del agenda[i]
                        print("O contato foi excluido!")
                        break
                    else:
                        print("Operação cancelada!")
        elif buscar == 2:
            busca = input("insira o e-mail referente ao contato que deseja excluir ou digite 0 para cancelar: ")
            for i, contato in enumerate(agenda):
                if busca == contato['email']:
                    print("Tem certeza que deseja excluir o seguinte contato? S/N")
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    ex = input(">")
                    if ex == 'S':
                        del agenda[i]
                        print("O contato foi excluido!")
                    else:
                        print("Operação cancelada!")
        elif buscar == 3:
            busca = input("insira o telefone referente ao contato que deseja excluir ou digite 0 para cancelar: ")
            for i, contato in enumerate(agenda):
                if busca == contato['tel']:
                    print("Tem certeza que deseja excluir o seguinte contato? S/N")
                    print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))
                    ex = input(">")
                    if ex == 'S':
                        del agenda[i]
                        print("O contato foi excluido!")
                    else:
                        print("Operação cancelada!")
        elif busca == 0:
            print("saindo...")

def listar(agenda): ## Listar todos os contatos

    print("Listar contatos")
    print("Nome\tE-mail\tTelefone")
    for contato in agenda:
        print("{}\t{}\t{}".format(contato['nome'], contato['email'], contato['tel']))

def menu(): ## definição do menu que puxa todas as funções
    agenda = carregar()

    while True:
        print("1 - Incluir novo contato")
        print("2 - Buscar contato")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Listar contatos")
        print("0 - Sair")
        opcao = int(input("Digite o numero referente a opção que deseja: "))

        if opcao == 1:
            incluir(agenda)
            salvar(agenda)
        elif opcao == 2:
            buscar(agenda)
        elif opcao == 3:
            editar(agenda)
            salvar(agenda)
        elif opcao == 4:
            excluir(agenda)
            salvar(agenda)
        elif opcao == 5:
            listar(agenda)
        elif opcao == 0:
            print("Sistema encerrado")
            salvar(agenda)
            break
        elif 1<opcao>5:
            print("Opção inválida!")

menu()  ## O programa é iniciado para o usuário

