nome = input("Informe se nome: ")
idade = int(input("Informe sua idade: "))

# Estrutura de Decisão - OPERADOR TERNARIO - para casos simples de decisao
result = "é Maior de idade"if idade >= 18 else "é menor de idade"
print(f"{nome} {result}")