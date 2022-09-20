def mostra_tela_inicial()->None:
    NUMERO_REPETICOES = 40
    print ('*' * NUMERO_REPETICOES)
    print ('Cardápio'.center(NUMERO_REPETICOES))
    print ('_' * NUMERO_REPETICOES)
    print('Código  /  Especificação  /   Preço'.center(NUMERO_REPETICOES))
    print ('_' * NUMERO_REPETICOES )

def mostra_menu(cardapio: dict):
    for chave, item in cardapio.items():
        print(f' {chave} / {item.descricao:20s} / R$ {item.preco:.2f}')

    print ('_' * 40 )


def mostra_pedido(cardapio: dict, pedido: dict):
    print ('Seu pedido possui:')    
    preco_total = 0
    for chave, item in pedido.items():
        if item > 0:
            produto = cardapio[chave]
            preco_produto = produto.preco * item
            preco_total += preco_produto
            print(f'{item} unidades de {produto.descricao} no total de R${preco_produto:.2f}')

    print(f'O total do seu pedido é de R${preco_total:.2f}')
