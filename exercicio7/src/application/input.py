from dataclasses import dataclass
from src.application.config import gabarito_prova


def entra_nome_aluno():
    
    while True:
        nome_aluno = input('Digite o nome do aluno:')
        nome_aluno_tratado = nome_aluno.replace(" ","")
        if not (nome_aluno_tratado != None and nome_aluno_tratado.isalpha()):
            print('É necessário colocar o nome do aluno') 
            continuar=input('Deseja continuar [S] ou [N]')
            if continuar.upper() == "S":
                continue 
            elif continuar.upper() == "N":
                print('Programa finalizado!')
                exit()
        else:
            return nome_aluno
    
    

def recebe_respostas():
    resposta_da_prova={}
    while True:
        for chave in gabarito_prova.keys():
            resposta = str(input(f"escolha a resposta da questão {chave}. \na---------\nb---------\nc---------\nd---------\ne---------\n"))
            resposta_da_prova[chave] = resposta
        return resposta_da_prova

        
                
    
    






