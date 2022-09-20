from src.application.config import indice_candidato,contagem_voto

def armazena_os_dados(voto):

    while voto != 0:
        voto_computado = indice_candidato.get(int(voto))
        contagem_voto[str(voto_computado)]+=1
        return "continue"

    if voto == 0:
        return "encerramento_votacao"


def calculo_porcentagem_votos_brancos(contagem_voto):

    total_votos = sum(contagem_voto.values())
    porcentagem_branco = contagem_voto['Voto em Branco'] * 100 / total_votos
    porcentagem_nulo = contagem_voto['Voto Nulo'] * 100 / total_votos

    return total_votos,porcentagem_branco,porcentagem_nulo

    


    



