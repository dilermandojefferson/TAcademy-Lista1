from src.application.input import complexo2
from src.application.domain import verificacao
from src.application.output import mostra


if __name__ == "__main__":
   
   entrada=complexo2()   
   entrada_salva=verificacao(entrada)
   mostra(entrada_salva)  