from dataclasses import dataclass


def calcula_media_saltos(lista_saltos:list)->float:
        copia_saltos = lista_saltos[:]
        copia_saltos.remove(max(copia_saltos))
        copia_saltos.remove(min(copia_saltos))

        media = sum(copia_saltos) / len(copia_saltos)

        return media

@dataclass
class Atletas:
    
    nome_atleta:str
    saltos_atleta:list[float]
    media: float
    conjunto_dados = []

    def salva_dados(nome:str,saltos:list,media:float):  # type: ignore
        Atletas.conjunto_dados.append(Atletas(nome_atleta=nome,saltos_atleta=saltos,media=media))

    