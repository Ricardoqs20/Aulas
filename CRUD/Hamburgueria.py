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
        
        # Variáveis para guardar os nomes dos itens escolhidos
        pao = ''
        carne = ''
        acomp1 = ''
        acomp2 = ''
        acomp3 = ''

        while True:
            print('1-Escolha o tipo de pão')
            print('Opções: 1- Pão de forma, 2- Pão de hambúrguer, 3- Pão integral')
            opcao_pao = int(input('Digite a opção desejada: '))
            if opcao_pao == 1:
                print('Pão de forma selecionado')
                pao = 'Pão de forma'
                break
            elif opcao_pao == 2:
                print('Pão de hambúrguer selecionado')
                pao = 'Pão de hambúrguer'
                break
            elif opcao_pao == 3:
                print('Pão integral selecionado')
                pao = 'Pão integral'
                break
            else:
                print('Opção inválida. Tente novamente.')
        
        while True:
            print('2-Escolha o tamanho da carne')
            print('Opções: 1- Carne 100g, 2- Carne 200g, 3- Carne 300g')
            opcao_carne = int(input('Digite a opção desejada: '))
            if opcao_carne == 1:
                print('Carne 100g selecionada')
                carne = 'Carne 100g'
                break
            elif opcao_carne == 2:
                print('Carne 200g selecionada')
                carne = 'Carne 200g'
                break
            elif opcao_carne == 3:
                print('Carne 300g selecionada')
                carne = 'Carne 300g'
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
                        acomp1 = 'Batata frita'
                        break
                    elif opcao_acompanhamento1 == 2:
                        print('Onion rings selecionado')
                        acomp1 = 'Onion rings'
                        break
                    elif opcao_acompanhamento1 == 3:
                        print('Salada selecionada')
                        acomp1 = 'Salada'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                break

            elif opcao_acompanhamento == 2:
                print('2 acompanhamentos selecionados')
                while True:
                    print('Escolha o primeiro acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento2 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento2 == 1:
                        print('Batata frita selecionada')
                        acomp1 = 'Batata frita'
                        break
                    elif opcao_acompanhamento2 == 2:
                        print('Onion rings selecionado')
                        acomp1 = 'Onion rings'
                        break
                    elif opcao_acompanhamento2 == 3:
                        print('Salada selecionada')
                        acomp1 = 'Salada'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                
                while True:
                    print('Escolha o segundo acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento3 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento3 == 1:
                        print('Batata frita selecionada')
                        acomp2 = 'Batata frita'
                        break
                    elif opcao_acompanhamento3 == 2:
                        print('Onion rings selecionado')
                        acomp2 = 'Onion rings'
                        break
                    elif opcao_acompanhamento3 == 3:
                        print('Salada selecionada')
                        acomp2 = 'Salada'
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
                        acomp1 = 'Batata frita'
                        break
                    elif opcao_acompanhamento4 == 2:
                        print('Onion rings selecionado')
                        acomp1 = 'Onion rings'
                        break
                    elif opcao_acompanhamento4 == 3:
                        print('Salada selecionada')
                        acomp1 = 'Salada'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                
                while True:
                    print('Escolha o segundo acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento5 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento5 == 1:
                        print('Batata frita selecionada')
                        acomp2 = 'Batata frita'
                        break
                    elif opcao_acompanhamento5 == 2:
                        print('Onion rings selecionado')
                        acomp2 = 'Onion rings'
                        break
                    elif opcao_acompanhamento5 == 3:
                        print('Salada selecionada')
                        acomp2 = 'Salada'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')

                while True:
                    print('Escolha o terceiro acompanhamento')
                    print('Opções: 1- Batata frita, 2- Onion rings, 3- Salada')
                    opcao_acompanhamento6 = int(input('Digite a opção desejada: '))
                    if opcao_acompanhamento6 == 1:
                        print('Batata frita selecionada')
                        acomp3 = 'Batata frita'
                        break
                    elif opcao_acompanhamento6 == 2:
                        print('Onion rings selecionado')
                        acomp3 = 'Onion rings'
                        break
                    elif opcao_acompanhamento6 == 3:
                        print('Salada selecionada')
                        acomp3 = 'Salada'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                break
            
            else:
                print('Opção inválida. Tente novamente.')

        if opcao_acompanhamento == 1:
            print(f'Seu hambúrguer personalizado ficou pronto! Ingredientes: {pao}, {carne} e {acomp1}.')
        elif opcao_acompanhamento == 2:
            print(f'Seu hambúrguer personalizado ficou pronto! Ingredientes: {pao}, {carne}, {acomp1} e {acomp2}.')
        elif opcao_acompanhamento == 3:
            print(f'Seu hambúrguer personalizado ficou pronto! Ingredientes: {pao}, {carne}, {acomp1}, {acomp2} e {acomp3}.')

    else:
        print('Opção inválida. Tente novamente.')