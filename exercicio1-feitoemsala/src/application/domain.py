from dataclasses import dataclass
from src.application.config import Imposto

@dataclass
class Salario:
    salario_bruto:float = 0

    def __init__(self,salario_bruto:float) -> None:
        if salario_bruto < 0:
            raise Exception("Salario não pode ser menor que zero!")
        self.salario_bruto = salario_bruto
    
    def valor_imposto_renda(self): return round(self.salario_bruto * Imposto.IMPOSTO_RENDA,2)
    def valor_inss(self): return round(self.salario_bruto * Imposto.INSS, 2)
    def valor_sindicato(self): return round(self.salario_bruto * Imposto.SINDICATO, 2)
    def salario_liquido(self): return self.salario_bruto - self.valor_imposto_renda() - self.valor_inss() - self.valor_sindicato()

