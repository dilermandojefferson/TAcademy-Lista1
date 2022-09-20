def pega_continua_pedido()-> str:
    while True:
        resposta = input('Deseja fazer mais algum pedido?\n S/N').upper()
        if resposta =='S':
            break
        elif resposta =='N':
            break
        else:
            print('opção invalida')
    return resposta

def pega_opcao_menu()->int:
    while True:
        opcao = int(input('Escolha a sua opcão:'))
        if (opcao < 100 or opcao > 105):   
            print('Opção invalida')

        else:
            break       
    return opcao

def pega_quantidade_desejada()->int:
    return int(input('Quantas unidades deseja?'))