def recebe_nota_total_melhor_pior_media():
    distancia_tds_saltos=[] 

    while len(distancia_tds_saltos) <= 4:
        distancia_tds_saltos.append(float(input('digite a nota do salto:  '))) 

    distancia_saltos_final = distancia_tds_saltos[:]

    maior_salto = max(distancia_saltos_final)
    pior_salto = min(distancia_saltos_final)
    distancia_saltos_final.remove(maior_salto)
    distancia_saltos_final.remove(pior_salto)
    media_distancia_final = sum(distancia_saltos_final) / len(distancia_saltos_final)


    return distancia_tds_saltos,media_distancia_final,maior_salto,pior_salto



def roda_programa(entra_nome_atleta,saida_print):
    nome_atleta = entra_nome_atleta()
    distancia_tds_saltos,media_distancia_final,maior_salto,pior_salto = recebe_nota_total_melhor_pior_media()
    saida_print(nome_atleta,distancia_tds_saltos = distancia_tds_saltos ,media_distancia_final = media_distancia_final,pior_salto = pior_salto,maior_salto = maior_salto)
