from src.application.config import QUANTIDADE_SALTOS


def recebe_nome_atleta()->str:
    while True:
        nome_atleta = input('Digite o nome do atleta:')
        atleta_nome_Tratado = nome_atleta.replace(" ","")
        if not (atleta_nome_Tratado !="none" and atleta_nome_Tratado.isalpha()):
            print('Nome digitado incorretamente, tente novamente')
        else:
            break
    return nome_atleta

def continuar_programa()->str:
    while True: 
        continuar_programa = input('Outro atleta irá saltar: [S] / [N]').upper()
        if (continuar_programa !="S") and (continuar_programa !="N"):
            print("Por favor digite apenas S ou N")
        elif continuar_programa == "S":
            break
        else:            
            break
    return continuar_programa
    
def recebe_saltos()->list:
    lista_saltos = []

    for i in range(1, QUANTIDADE_SALTOS + 1):
        while True:
            try:
                saltos = float(input(f'{i}º salto: '))
                break
            except:
                print("Por favor digite uma nota válida")
        
        lista_saltos.append(saltos)
                
    return lista_saltos