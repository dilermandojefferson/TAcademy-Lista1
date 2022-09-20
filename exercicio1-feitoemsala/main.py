
from src.application.input import pega_dados_para_calculo_do_salario
from src.application.domain import Salario
from src.application.output import mostra_salario
if __name__ == '__main__':
    info = pega_dados_para_calculo_do_salario()
    try:
        salario = Salario(info.horas_trabalho * info.salario_hora)
    except Exception as erro:
        print('ERRO!')
    mostra_salario(salario)
    