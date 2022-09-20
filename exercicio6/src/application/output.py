from src.application.config import contagem_voto

def exibe_candidato():
    print (f'Opções e cadidatos:\n1  João\n2  Maria\n3  Bolso\n4  Lulinha\n5  Voto Nulo\n6  Voto em Branco\n')
    


def exibe_resultado(total_votos, porcentagem_branco,porcentagem_nulo):
    print("Votação encerrada")
    print(f"O candidato João recebeu {contagem_voto['João']} votos.\nA candidata Maria recebeu {contagem_voto['Maria']} votos. \nO candidato Bolso recebeu {contagem_voto['Bolso']}votos. \nO candidato Lulinha recebeu {contagem_voto['Lulinha']}votos. \nTiveram {contagem_voto['Voto Nulo']} votos nulos e {contagem_voto['Voto em Branco']} em branco ") 
    print(f'O total de votos foi de {total_votos} votos.')
    if porcentagem_branco > 0:
        print(f'A porcentagem de votos em Branco é de {porcentagem_branco:.2f}%')
    if porcentagem_nulo > 0:
        print(f'A porcentagem de votos Nulo é de {porcentagem_nulo:.2f}%')
        
   