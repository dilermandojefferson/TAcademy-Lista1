def entrada_atleta()->str:
    while True:
        atleta_nome = input('Digite o nome do atleta:')
        atleta_nome_Tratado = atleta_nome.replace(" ","")
        if not (atleta_nome_Tratado !="none" and atleta_nome_Tratado.isalpha()):
            print('Nome digitado incorretamente, tente novamente')

        else:
            break
    return atleta_nome        
