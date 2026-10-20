print('Bem vindo á Hamburgueria')
                                                                                                 
while True:
    print('1-Quero um hamburguer simples')
    print('2-Quero um hamburguer duplo')
    print('3-Quero um hamburguer triplo')
    print('4-Quero montar meu hamburguer')
    print('5-Quero sair')
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 5:
        break

    elif opcao == 1:
        print('Hamburguer simples')
        print('Ingredientes: Pão, carne, queijo, alface e ovo')
        print('Preço: R$ 15,00')

    elif opcao == 2:
        print('Hamburguer duplo')
        print('Ingredientes: Pão, 2 carnes, queijo, alface e ovo')
        print('Preço: R$ 20,00')

    elif opcao == 3:
        print('Hamburguer triplo')
        print('Ingredientes: Pão, 3 carnes, queijo, alface e ovo')
        print('Preço: R$ 25,00')

    elif opcao == 4:
        print('Montar meu hamburguer')
        

        while True:
            print('1-Escolha o tipo de pão')
            print('Opções: 1- Pão de forma, 2- Pão de hambúrguer, 3- Pão integral')
            opcao_pao = int(input('Digite a opção desejada: '))
            if opcao_pao == 1:
                print('Pão de forma selecionado')
                break
            elif opcao_pao == 2:
                print('Pão de hambúrguer selecionado')
                break
            elif opcao_pao == 3:
                print('Pão integral selecionado')
                break
            else:
                print('Opção inválida. Tente novamente.')
        
        while True:
            print('2-Escolha o tamanho da carne')
            print('Opções: 1- Carne 100g, 2- Carne 200g, 3- Carne 300g')
            opcao_carne = int(input('Digite a opção desejada: '))
            if opcao_carne == 1:
                print('Carne 100g selecionada')
                break
            elif opcao_carne == 2:
                print('Carne 200g selecionada')
                break
            elif opcao_carne == 3:
                print('Carne 300g selecionada')
                break
            else:
                print('Opção inválida. Tente novamente.')
        
        while True:
            print('3-Escolha a quantidade de acompanhamentos')
            print('Opções: 1 acompanhamento, 2 acompanhamentos, 3 acompanhamentos')
            opcao_acompanhamento = int(input('Digite a opção desejada: '))
            
            if opcao_acompanhamento == 1:
                print('1 acompanhamento selecionado')
                while True:
                    print('Escolha o acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento1 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento1 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento1 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento1 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                break # Sai do loop de quantidade de acompanhamentos

            elif opcao_acompanhamento == 2:
                print('2 acompanhamentos selecionados')
                while True:
                    print('Escolha o primeiro acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento2 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento2 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento2 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento2 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                
                while True:
                    print('Escolha o segundo acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento3 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento3 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento3 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento3 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                break

            elif opcao_acompanhamento == 3:
                print('3 acompanhamentos selecionados')
                while True:
                    print('Escolha o primeiro acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento4 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento4 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento4 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento4 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                
                while True:
                    print('Escolha o segundo acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento5 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento5 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento5 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento5 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')

                while True:
                    print('Escolha o terceiro acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento6 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento6 == 1:
                        print('Batata frita selecionada')
                        break
                    elif opcao_acompanhamento6 == 2:
                        print('Onion rings selecionado')
                        break
                    elif opcao_acompanhamento6 == 3:
                        print('Salada selecionada')
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                break
            
            else:
                print('Opção inválida. Tente novamente.')

    else:
        print('Opção inválida. Tente novamente.')