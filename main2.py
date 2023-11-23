agenda = {}
while True:
    print('---AGENDA TELEFONICA---')
    print('1 - Adicionar contato')
    print('2 - Editar telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')
    opcao = input('Selecione uma opção: ')
    if opcao == "1":
        nome=input('Informe o nome do contato: ')
        if nome not in agenda:
            numero=input('Informe o numero do contato: ')
            agenda[nome]=numero
            print('Contato adicionado com sucesso!')
        else:
            print('Contato já existe na agenda!')
    if opcao == "2":
        nome=input('Informe o contato que deseja editar: ')
        if nome in agenda:
            numero=input('Informe o numero correto ')
            agenda[nome]=numero
        else:
            print('Esse contato não existe!')
    if opcao == "3":
        nome=input('Informe o contato a ser excluido: ')
        if nome in agenda:
            del agenda [nome]
        else:
            print('Esse contato não existe na agenda!')
    if opcao == "4":
        nome=input('Informe o nome que deseja buscar! ')
        if nome in agenda:
            print({agenda[nome]})
        else:
            print('Esse contato não existe!')
    if opcao == "5":
        print(agenda)
    if opcao == "6":
        break