import math ## base matematica
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def primeiro_grau(a, b):
    # a*x + b = 0   ## isola o X e troca  a ordem das letras
    x = -b / a
    return x

def segundo_grau(a, b, c):
    ## a*x² + b*x + c = 0       ## A nunca pode ser = 0
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:   ## se delta for maior que 0, tem duas raizes possiveis para X
            x1 = (-b + math.sqrt(delta)) / (2*a)    ## função para raiz quadrada de X1
            x2 = (-b - math.sqrt(delta)) / (2*a)    ## função para raiz quadrada de X2

            yield f"x' = {x1}"    # yield opção avançada para o return , com mais de uma opção
            yield f'x" = {x2}'

        elif delta == 0:
            yield "Não há Raizes Reais para X"

        else:
            x = -b/(2*a)     
            yield x   

    else:
        yield primeiro_grau(b, c)