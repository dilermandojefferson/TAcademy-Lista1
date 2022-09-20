from src.application.negocio import download_time
from src.application.output import mostra_resultados
from src.application.input  import entrada_dados


if __name__ == '__main__':
    dados  = entrada_dados()
    tempo_de_download = download_time(dados)
    mostra_resultados(tempo_de_download)