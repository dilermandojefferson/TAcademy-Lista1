from dataclasses import dataclass
from typing import List

@dataclass
class ItemCardapio:
    descricao: str = ""
    preco: float = 0


def monta_cardapio()->dict:
    cardapio = dict()

    cardapio[100] = ItemCardapio("Cachorro Quente", 1.20)
    cardapio[101] = ItemCardapio("Bauru Simples", 1.30)
    cardapio[102]= ItemCardapio("Bauru com ovo", 1.50)
    cardapio[103]= ItemCardapio("Hambúrguer", 1.20)
    cardapio[104]= ItemCardapio("Cheeseburguer", 1.30)
    cardapio[105]= ItemCardapio("Refrigerante", 1.00)

    return cardapio

def inicia_pedido(cardapio: dict)->dict:
    retorno = dict()

    for chave in cardapio:
        retorno[chave] = 0
        
    return retorno

