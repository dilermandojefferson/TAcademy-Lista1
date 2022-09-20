from src.application.input import pega_salario_e_hora
from src.application.domain import calcula_salario_bruto,calculo_impostos
from src.application.output import mostra_resultado

if __name__=="__main__":
    valores  = pega_salario_e_hora()
    salariobruto = calcula_salario_bruto(valores)
    Desconto = calculo_impostos(salariobruto)
    mostra_resultado(salariobruto,Desconto)



