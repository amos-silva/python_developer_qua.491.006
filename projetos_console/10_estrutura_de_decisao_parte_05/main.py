# Calculadora

print(f"\n{'-'*20} INFORME OS NUMEROS QUE DESEJA FAZER O CALCULO {'-'*20}\n")

x = float(input("informe o valor de X: ").replace(",", "."))
y = float(input("informe o valor de Y: ").replace(",", "."))

#MENU
print(f"\n{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")  # \n quebra linha e {'-'*20} criar linha com traços de tamanho 20
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão \n")

operador = input("Informe a operação desejada: ").strip()   # strip serve para eliminar valor nulo, EX: espaço

# match case - PARA ESCOLHA DE VÁRIAS OPÇÕES
match operador:
    case "1":
        print(f"A SOMA dos valores é: {x+y}")
    case "2":
        print(f"A SUBTRAÇÃO dos valores é: {x-y}")
    case "3":
        print(f"A MULTIPLICAÇÃO dos valores é: {x*y}")
    case "4":
        print(f"A DIVISÃO dos valores é: {x/y}")
    case _: # CASE Default - se digitar algo diferente do que eu pedi
        print("OPERAÇÃO INVÁLIDA - ESCOLHA UMA DAS 4 OPERAÇÕES")
