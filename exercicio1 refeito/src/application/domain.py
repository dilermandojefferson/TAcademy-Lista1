from dataclasses import dataclass
from src.application.config import DESCONTOIMPOSTODERENDA,DESCONTOINSS,DESCONTOSINDICATO


def calcula_salario_bruto(valor_hora_mes)->float:
    salariobruto = valor_hora_mes.salario_hora * valor_hora_mes.hora_mes
    return salariobruto


@dataclass
class ValoresDesconto:
    desconto_ir:float = 0
    desconto_inss:float = 0
    desconto_sindicato:float = 0
    salario_liquido:float = 0


def calculo_impostos(salariobruto:float):
    valores_desconto = ValoresDesconto()
    valores_desconto.desconto_ir = salariobruto * DESCONTOIMPOSTODERENDA
    valores_desconto.desconto_inss = salariobruto * DESCONTOINSS
    valores_desconto.desconto_sindicato = salariobruto * DESCONTOSINDICATO
    valores_desconto.salario_liquido = salariobruto - (valores_desconto.desconto_ir + valores_desconto.desconto_inss + valores_desconto.desconto_sindicato)

    return valores_desconto