from src.application.domain2 import abre_arquivo_exchange,abre_arquivo_bitcoin,juntando_as_listas,compras_e_vendas
from src.application.output import mostra_resultado


if __name__ == "__main__":
    lista_bitcoin=abre_arquivo_bitcoin()
    lista_exchange=abre_arquivo_exchange()
    merge_listas=juntando_as_listas(lista_bitcoin,lista_exchange)
    compras_total,venda_total,saldo_total=compras_e_vendas(merge_listas)
    mostra_resultado(merge_listas,compras_total,venda_total,saldo_total)
    