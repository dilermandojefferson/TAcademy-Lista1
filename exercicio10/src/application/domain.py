def tratamento_nota_jurados():
    conjunto_notas = []
    for i in range(7):
        conjunto_notas.append (float(input("Qual a nota do atleta: ")))
      

    conjunto_notas_final = conjunto_notas[:]

    melhor_nota = max(conjunto_notas_final)
    pior_nota = min(conjunto_notas_final)    
    conjunto_notas_final.remove(melhor_nota)
    conjunto_notas_final.remove(pior_nota)
    media_notas_final = sum(conjunto_notas_final)/len(conjunto_notas_final)


      
    return conjunto_notas,melhor_nota,pior_nota,media_notas_final








def roda_programa(entrada_atleta,saida_print):
    atleta_nome = entrada_atleta()  
    conjunto_notas,melhor_nota,pior_nota,media_notas_final = tratamento_nota_jurados() 
    saida_print(atleta_nome ,conjunto_notas,melhor_nota,pior_nota,media_notas_final)    