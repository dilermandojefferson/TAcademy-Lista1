from src.application.input import continuar_programa, recebe_nome_atleta, recebe_saltos
from src.application.domain import Atletas,calcula_media_saltos
from src.application.output import mostra_resultado



if __name__=='__main__':
    while True:
        nome_atleta = recebe_nome_atleta()
        saltos_atleta = recebe_saltos()
        media=calcula_media_saltos(saltos_atleta)
        Atletas.salva_dados(nome_atleta,saltos_atleta,media)  # type: ignore
        continuar_sistema = continuar_programa()
        if continuar_sistema.upper() == "S":
            continue
        else:
            mostra_resultado(Atletas.conjunto_dados)
            break