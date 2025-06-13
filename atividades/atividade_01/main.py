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

    gas = float(input("Informe valor da Gasolina: ").replace(",", "."))
    eta = float(input("Informe valor do Etanol: ").replace(",", "."))

    gas_calc = gas * 0.7
    result = eta - gas_calc

    if eta < gas_calc:
        print(f" Etanol (30%) {result} a menos que a Gasolina -  VALE A PENA ABASTERNCER COM ETANOL.")
    else:
        print(f"Melhor abastecer com Gasolina.")