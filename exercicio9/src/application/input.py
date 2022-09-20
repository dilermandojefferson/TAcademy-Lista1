def entra_nome_atleta()->str:
    while True:
        nome_atleta = input('Digite o nome do atleta:')
        nome_atleta_tratado = nome_atleta.replace(" ","")
        if not (nome_atleta_tratado != None and nome_atleta_tratado.isalpha()):
            print('É necessário colocar o nome do atleta') 
            continuar=input('Deseja continuar [S] ou [N]')
            if continuar.upper() == "S":
                continue 
            elif continuar.upper() == "N":
                print('Programa finalizado!')
                exit()
        else:
            break
    
    return nome_atleta