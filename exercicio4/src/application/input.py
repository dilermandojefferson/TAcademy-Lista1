from dataclasses import dataclass


@dataclass
class TamanhoVelocidade():
    tamanho_arquivo:float = 0
    velocidade_download:float = 0
def entrada_dados():
    dados_entrada = TamanhoVelocidade()
    dados_entrada.tamamaho_arquivo = float(input('Digite o tamanho do arquivo em MB/s : '))
    dados_entrada.velocidade_download  = float(input('Velocidad da internet : '))
    return dados_entrada
