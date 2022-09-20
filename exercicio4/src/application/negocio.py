def download_time(dados_entrada):
    tempo_de_download = dados_entrada.tamamaho_arquivo/(dados_entrada.velocidade_download/8)/60
    return tempo_de_download