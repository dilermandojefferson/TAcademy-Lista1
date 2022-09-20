from src.application.domain import armazena_os_dados
def funcao_votar():

    while True:
        voto = input('Insira o seu voto: ')
        if not ((voto == '1') or (voto == '2') or (voto == '3') or (voto == '4') or (voto == '5') or (voto == '6') or (voto == '0')):
            print('Opção inválida, tente novamente, por favor')
            
        else:
            return int(voto)
            
def funcao_encerramento():
    while True:
        senha = input('Opção somente para pessoas autorizadas \nDigite a senha de segurança: ')
        if senha == 'seguranca':
            return 'Opcão de encerramento solicitada'

        else:  
            opcao_voltar = input("Senha errada, tente novamente(ou digite voltar para voltar a votação)")
            if opcao_voltar == 'seguranca':
                return 'Opcão de encerramento solicitada'
            elif opcao_voltar == 'voltar':
                return 'voltando'
            
           





            
             

        
            
                
            
            
    
                        
