def saida_print(nome_atleta:str ,distancia_tds_saltos:list,media_distancia_final:float,maior_salto,pior_salto:float):
    print(f'Atleta: {nome_atleta}\nPrimeiro Salto: {distancia_tds_saltos[0]}M\nSegundo Salto: {distancia_tds_saltos[1]}M\nTerceiro Salto: {distancia_tds_saltos[2]}M\nQuarto Salto: {distancia_tds_saltos[3]}M\nQuinto Salto: {distancia_tds_saltos[4]}M\nMelhor salto: {maior_salto}M\nPior salto: {pior_salto}M\nMédia dos demais saltos: {media_distancia_final:.2f}M\nResultado Final:\n{nome_atleta}: {media_distancia_final:.2f}M')
    
  