def abre_arquivo_bitcoin():
    lista_bitcoin = []

    with open("asset/bitcoin.txt","r") as arquivo1:
        linhas = arquivo1.readlines()
        for linha in linhas:
            linha = linha.replace('\n',"").split(';')
            lista_bitcoin.append(linha)
    return lista_bitcoin

def abre_arquivo_exchange():
    lista_exchange = []

    with open("asset/exchange.txt","r") as arquivo2:
        linhas = arquivo2.readlines()
        for linha in linhas:
            linha = linha.replace('\n',"").split(';')
            lista_exchange.append(linha)
    return lista_exchange   

def juntando_as_listas(lista_bitcoin,lista_exchange):
    merge_listas = lista_bitcoin + lista_exchange
    merge_listas.sort()
    
    return merge_listas
    

def compras_e_vendas(merge_listas):
    compra=[]
    venda = []
    for linha in merge_listas: 
        if linha[1] == 'compra':
            compra.append(linha[2])

        if linha[1] == 'venda':
            venda.append(linha[2])

    compras_total = list(map(int, compra)) 
    venda_total = list(map(int, venda))

    saldo_total = sum(compras_total) - sum(venda_total)

    return sum(compras_total),sum(venda_total),saldo_total
