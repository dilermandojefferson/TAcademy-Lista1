from dataclasses import dataclass
from src.application.config import gabarito_prova


@dataclass
class AcertosErros:

    acertos:int = 0
    erros:int = 0


def confere_resposta(resposta_da_prova:dict):
    acerto_erro_questao = AcertosErros()

    
    for chave in gabarito_prova:
        if (chave in resposta_da_prova) and (gabarito_prova[chave] == resposta_da_prova[chave]):   
            acerto_erro_questao.acertos+=1
        else:
            acerto_erro_questao.erros+=1

    return acerto_erro_questao

def salva_nome_do_aluno(nome_aluno:str,acerto_erro_questao:AcertosErros)->dict:

    dict_nomes_e_notas={}
    
    dict_nomes_e_notas[nome_aluno] = acerto_erro_questao.acertos
        

    return dict_nomes_e_notas


