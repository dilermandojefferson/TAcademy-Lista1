from optparse import Values
from src.application.config import gabarito_prova
from src.application.domain import confere_resposta,salva_nome_do_aluno
from src.application.input import recebe_respostas,entra_nome_aluno
from src.application.output import resultado_individual





if __name__ == "__main__":

    nomes_salvos={}
    while True:
        nome_aluno=entra_nome_aluno()
        resposta=recebe_respostas()
        resultado=confere_resposta(resposta)
        resultado_individual(resultado)
        resultado_salvo=salva_nome_do_aluno(nome_aluno,resultado)
        nomes_salvos.update(resultado_salvo)
        continuar = input("Deseja continuar S ou N")
        if continuar.upper() == "S":
            continue 
        elif continuar.upper() == "N":
            break
    print("alunos que fizeram a prova")  
    for keys, values in nomes_salvos.items():
        print(f"aluno {keys} acertou {values} questões")
