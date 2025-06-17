#   math    funções matematicas
import math as m
print(f"Numero de PI: {m.pi}")

#Raiz quadrada
try:
    num = int(input("Numero inteiro: "))
    print(f"a raiz quadrada de {num} é: {m.sqrt(num)}")
except Exception as e:
    print(f"Não foi possivel calcular. {e}")
