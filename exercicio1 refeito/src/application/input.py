from dataclasses import dataclass
@dataclass
class HoraeMes:
    salario_hora:float = 0
    hora_mes:float = 0

def pega_salario_e_hora():
    valor_hora_mes = HoraeMes()
    valor_hora_mes.salario_hora = float(input('Quanto você ganha por hora? R$'))
    valor_hora_mes.hora_mes= float(input('Quantas horas você trabalha por mês?'))

    return valor_hora_mes   
