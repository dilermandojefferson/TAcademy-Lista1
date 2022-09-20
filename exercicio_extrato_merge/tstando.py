from dataclasses import dataclass
from typing import Any


if __name__ == "__main__":

    @dataclass
    class Opcoes:
        num_opcao: int
        nome_opcao: str

        def _getitem_(self, key):
            return self.__dict__[key]

    def recebe_arquivo(file_name: str)->Any:
        lista = []

        with open(file_name, newline='') as inputfile:
            linhas = inputfile.readlines()
            for linha in linhas:
                linha = linha.replace('\r\n', '')
                campos = linha.split(';')
                tratamento_opcoes = Opcoes(int(campos[0]), campos[1])
                lista.append(tratamento_opcoes)
            # ultima_opcao = len(lista) + 1
            # lista.append((ultima_opcao[0], 'Sair do Menu'[1]))
        return lista

    def mostra_menu(lista_opcoes: list):
        tamanho_opcoes = len(lista_opcoes)
        c = 0
        for i in range(0, tamanho_opcoes):
            print(lista_opcoes[i]['num_opcao'], lista_opcoes[i]['nome_opcao'])
            c += 1
        print((c+1), 'Sair do Menu')

    def seleciona_opcao_menu(lista_de_opcoes: list):
        lista_de_opcoes = lista_de_opcoes
        escolhe_opcao = input(f'\nINSIRA A OPÇÃO DESEJADA DO MENU')
        try:
            escolhe_opcao = int(escolhe_opcao)
        except:
            print('Por favor, insira um comando da lista')
        # tratamento = True
        # while tratamento == True:
        #     if type(escolhe_opcao) == int:
        #         tratamento = False
        #     else:
        #         print('Por favor, insira um comando da lista.')
        #         continue
        numero_de_opcoes_para_range = len(lista_de_opcoes) + 1
        contador = 0
        while True:
            for i in range(1, numero_de_opcoes_para_range):
                if escolhe_opcao != i:
                    contador += 1
                    #print('Por favor, insira um comando da lista.')
                    continue
                else:
                    break
            if contador > numero_de_opcoes_para_range:
                print('Por favor, insira um comando da lista.')
                continue
            else:
                break
        return escolhe_opcao

    lista_opecao = recebe_arquivo('arquivo_menu.txt')
    mostra_menu(lista_opecao)
    seleciona_opcao_menu(lista_opecao)