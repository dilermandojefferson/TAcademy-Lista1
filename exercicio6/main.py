from src.application.input import funcao_votar,funcao_encerramento
from src.application.domain import armazena_os_dados,calculo_porcentagem_votos_brancos
from src.application.output import exibe_candidato,exibe_resultado
from src.application.config import contagem_voto
if __name__ == "__main__":
    while True:
        exibe_candidato()
        voto=funcao_votar()
        if armazena_os_dados(voto) == "continue":
            continue
        elif armazena_os_dados(voto) == "encerramento_votacao": 
            if funcao_encerramento() == 'Opcão de encerramento solicitada':
                print('Opcão de encerramento solicitada \nRESULTADO:')
                break

        elif funcao_encerramento() == 'voltando':
            continue


    total_votos, porcentagem_branco,porcentagem_nulo=calculo_porcentagem_votos_brancos(contagem_voto)    
    exibe_resultado(total_votos, porcentagem_branco,porcentagem_nulo)
        
        
        
              

    
    
    

    


        



