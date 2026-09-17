comecar=input('Você deseja montar um misto? ')
if comecar==('sim'):
    while True:
        carboidrato=input('Primeiro carboidrato ')
        proteina1=input('Primeira proteina ')
        proteina2=input('Segunda proteina ')
        alimentos=[carboidrato,proteina1,proteina2]
        print(f'Seu misto é composto por {alimentos}')
        continuar=input('Você deseja continuar? Digite sim ou não ')

        if continuar==('não'):
            break
        elif continuar==('sim'):
            print('Proximó misto')
        else: 
            print('Essa opção não existe')
            break
elif comecar==('não'):
    print('Ok')
else: 
    print('Essa função não existe')