def mostra_resultado(merge_listas,compras_total,venda_total,saldo_total):
    print('Data       Operação   Quantidade')
    for linha in merge_listas:
        linhas = ("   ".join(linha))
        print(linhas)

        
    print(f'Seu total de compras foi {compras_total}\nSeu total de vendas foi {venda_total}\nSeu saldo é de {saldo_total} unidades.')

