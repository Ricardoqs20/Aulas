cadastrado = False
opcao = -1

while opcao != 0:
    print("\n===== CRUD NETFLIX =====")
    print("1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Atualizar filme")
    print("4 - Excluir filme")
    print("0 - Sair")

    opcao = int(input("Digite o número da opção: "))

    if opcao == 1:
        nome = input("Digite o nome do filme: ")
        duracao = int(input("Digite a duração em minutos: "))
        genero = input("Digite o gênero do filme: ")
        sinopse = input("Digite a sinopse: ")
        ano = int(input("Qual o ano de lançamento? "))
        nota = float(input("Qual é a nota? "))

        cadastrado = True
        print("Filme cadastrado com sucesso!")

    elif opcao == 2:
        if cadastrado:
            print("\n===== DADOS DO FILME =====")
            print("Nome:", nome)
            print("Duração:", duracao, "minutos")
            print("Gênero:", genero)
            print("Sinopse:", sinopse)
            print("Ano de lançamento:", ano)
            print("Nota:", nota)
        else:
            print("Nenhum filme cadastrado!")

    elif opcao == 3:
        if cadastrado:
            subopcao = -1

            while subopcao != 0:
                print("\n===== ATUALIZAR FILME =====")
                print("1 - Nome:", nome)
                print("2 - Duração:", duracao)
                print("3 - Gênero:", genero)
                print("4 - Sinopse:", sinopse)
                print("5 - Ano:", ano)
                print("6 - Nota:", nota)
                print("0 - Voltar ao menu principal")

                subopcao = int(input("Qual campo deseja atualizar? "))

                if subopcao == 1:
                    nome = input("Digite o novo nome: ")
                    print("Nome atualizado!")

                elif subopcao == 2:
                    duracao = int(input("Digite a nova duração em minutos: "))
                    print("Duração atualizada!")

                elif subopcao == 3:
                    genero = input("Digite o novo gênero: ")
                    print("Gênero atualizado!")

                elif subopcao == 4:
                    sinopse = input("Digite a nova sinopse: ")
                    print("Sinopse atualizada!")

                elif subopcao == 5:
                    ano = int(input("Digite o novo ano: "))
                    print("Ano atualizado!")

                elif subopcao == 6:
                    nota = float(input("Digite a nova nota: "))
                    print("Nota atualizada!")

                elif subopcao == 0:
                    print("Voltando ao menu principal...")

                else:
                    print("Opção inválida!")

        else:
            print("Nenhum filme cadastrado!")

    elif opcao == 4:
        if cadastrado:
            print("\n===== EXCLUIR FILME =====")
            print("Filme:", nome)

            confirmacao = input("Deseja excluir este filme? (s/n): ")

            if confirmacao == "s":
                cadastrado = False
                print("Filme excluído!")
            else:
                print("Exclusão cancelada!")

        else:
            print("Nenhum filme cadastrado!")

    elif opcao == 0:
        print("Encerrando o CRUD Netflix...")

    else:
        print("Opção inválida!")

print("Programa encerrado.")