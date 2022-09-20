def mostra_resultados(tempo_de_download:float):
    if tempo_de_download > 1:
        print(f'O Tempo de Download será de aproximadamente:{tempo_de_download:.2f} minutos')
    if tempo_de_download < 1: 
        print(f'O Tempo de Download será de aproximadamente:{tempo_de_download:.2f} segundos')