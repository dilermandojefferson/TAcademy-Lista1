from src.application.domain import monta_cardapio,inicia_pedido
from src.application.input import pega_continua_pedido, pega_opcao_menu, pega_quantidade_desejada
from src.application.output import mostra_menu, mostra_pedido, mostra_tela_inicial


if __name__ == '__main__':
    cardapio = monta_cardapio()
    pedido = inicia_pedido(cardapio)
    opcoes_validas = [key for key in cardapio.items()]

    mostra_tela_inicial()
    
    
    while (True):
        mostra_menu(cardapio)    

        opcao = pega_opcao_menu() 
        if (opcao in opcoes_validas):
            pedido[opcao] += pega_quantidade_desejada() 
            if pega_continua_pedido() == 'N': break
        else: print ('Opção invalida')

    mostra_pedido(cardapio,pedido)
