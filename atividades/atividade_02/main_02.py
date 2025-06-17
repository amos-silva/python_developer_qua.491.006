"""
Programa que recebe Nome, Peso e Altura e calcule o IMC.
mostrar o valor do IMC em duas casas decimais, e mostrar o diagnostico:

caso o valor seja menor que 18.5 = abaixo do pelo
caso o valor seja maior ou igual 18.5 e menor que 25 = peso ideal
caso o valor seja maior ou igual 25 e menor que 30 = acima do peso
caso o valor seja maior ou igual 30 e menor que 35 = obeso
caso o valor seja maior ou igual 35 e menor que 40 = obesidade nivel-2
caso o valor seja maior ou igual a 40 = obesidade morbita

o usuario pode repetir o calculo quantas vezes quiser, ou encerrar o programa
"""

while True:     # Laço de Repetição - while True
    
        
    try:        # Tratamento de Exceção - try / except  - Caso digite algo errado

        nome = input("informe seu nome: ").title().strip()      # title para primeira letra Maiuscula / strip para caracter invalido
        peso = float(input("Informe seu Peso: ").replace(",", "."))     # replace para converter , em .
        alt = float(input("Informe sua Altura: ").replace(",", "."))
     
        imc = peso/(alt**2)   
          
        if imc <18.5:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta ABAIXO do peso")    # :. 2f  casas decimais no numero

        elif imc >=18.5 and imc <25:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta no peso IDEAL")

        elif imc >=25 and imc <30:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta ACIMA do peso")

        elif imc >=30 and imc <35:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta OBESO")

        elif imc >=35 and imc <40:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta OBESO - Nivel 2")

        elif imc >=40:
            print(f"o valor do IMC é: {imc:.2f} - Voce esta com OBESIDADE MORBITA")

        else:
            print("ACIMA")    

        while True:
            opcao = input("Novo calculo? S / N : ").lower().strip()    # louwer para digitos minusculos ou maisculos / strip para caracter invalido
            if opcao == "s" or opcao == "n":
                break
            else:
                print("Opção inválida")
                continue

        match opcao:        # match e case , usa para varias opções
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção invalida")
                continue
    except Exception as e:
        print(f"Não foi possivel executar a operação.{e}")    
        continue
