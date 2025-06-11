nome = input("Informe se nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua Altura: ").replace(",", "."))   # replace converte um caracter = ( , em . )

# Estrutura de Decisão - mais de uma condição
if idade >=12 and altura >= 1.15:
    print(f"{nome} está liberado.")
else:
    print(f"{nome} NÃO está liberado, não cumpre um dos requisitos.")