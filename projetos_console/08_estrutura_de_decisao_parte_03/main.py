nome = input("Informe o nome do aluno: ")
media = float(input("Informe a média do aluno: ").replace(",", "."))   # replace converte um caracter = ( , em . )

# Estrutura de Decisão - mais de duas condição
if media >= 0 and media <=10:
    if media >=7:
        print(f"{nome} APROVADO")
    elif media >=5:
        print(f"{nome} está em Recuperação")   
    else:
        print(f"{nome} está REPROVADO")
else:
    print("Nota inválida")