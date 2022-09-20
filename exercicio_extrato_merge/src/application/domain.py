from dataclasses import dataclass
from typing import Any

@dataclass
class Movimentacao:
    data: str
    tipo: str
    quantidade: float

def get_list(file_name: str)->Any:
    list = []
    
    with open(file_name, newline='') as inputfile:
        linhas = inputfile.readlines()
        for linha in linhas:
            linha = linha.replace('\r\n', '')
            campos = linha.split(';')
            bitcoin = Movimentacao(campos[0], campos[1], float(campos[2]))

            list.append(bitcoin)
    return list

list_bitcoin = get_list("asset/bitcoin.txt")
saldo = 0
for el in list_bitcoin:

    if (el.tipo == 'venda'): saldo = saldo -el.quantidade
    else: saldo = saldo + el.quantidade

print (saldo) 

print (list_bitcoin)

 




