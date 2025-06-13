"""
Criar programa que receba os valores de alcool e gasolina em reais.
e informe qual melhor combustivel para abastecer
O usuario pode repetir várias vezes e encerrar o programa quando desejar.
calculo: compensa etanol caso ele tenha até 70% do valor da gasolina. - seja 30% mais barato que a gasolina

"""

while True:
    print(f"{'-'*20} Comparar Preço de Combustiveis {'-'*20} \n")
    print("0 - para SAIR")
    print("1 - para CONTINUAR")

    operador = input("Continuar ou Sair: ").strip()   
