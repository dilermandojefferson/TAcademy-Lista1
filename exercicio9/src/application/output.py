
def mostra_resultado(conjuto_dados:list):
    print("-"*20)
    for atletas in conjuto_dados:    
        print(f'Atleta: {atletas.nome_atleta}')
        for salto in atletas.saltos_atleta:
            print(f'{salto} m')

        print(f'Melhor salto: {max(atletas.saltos_atleta)} m')
        print(f'Pior salto: {min(atletas.saltos_atleta)} m')
        print(f'Média dos demais saltos: {atletas.media:.2f} m')
        print("")
        print('Resultado final:')
        print(f'{atletas.nome_atleta}: {atletas.media:.2f} m')
        print("-"*20)
