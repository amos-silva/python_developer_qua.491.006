import os
import time
import datetime
from datetime import date

nome = input("Informe seu nome: ")
idade = int(input("Sua idade: "))
dia = date.today().strftime("%d/%m/%Y") #converter data para Brasil
hora = datetime.datetime.now().strftime("%H:%M:%S")

while True:
    try:  
        print("----- MENU DE FILMES ----- \n")
        print("Sala-1: A Roda Quadrada - Livre")
        print("Sala-2: A Volta dos que não Foram - 12 anos")
        print("Sala-3: Poeira em Alto Mar - 14 anos")
        print("Sala-4: As Tranças do Rei Careca - 16 anos")
        print("Sala-5: A Vingança do Peixe Frito - 18 anos")

        sala = int(input("Informe a Sala: "))


        match sala:        # match e case , usa para varias opções
            case "1":
                if idade >=1:
                    print(f"Nomee: {nome}, Sala: {sala}, Filme: A Roda Quadrada - Livre.")
                    print(f"Bom Filme - Data: {dia} Hora: {hora}")
                continue
            case "2":
                continue
            case "3":
                continue
            case "4":
                continue
            case "5":
                continue
            case _:
                print("Opção invalida")
                continue
    

    #         if idade <18.5:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta ABAIXO do peso")    # :. 2f  casas decimais no numero

    #     elif imc >=18.5 and imc <25:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta no peso IDEAL")

    #     elif imc >=25 and imc <30:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta ACIMA do peso")

    #     elif imc >=30 and imc <35:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta OBESO")

    #     elif imc >=35 and imc <40:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta OBESO - Nivel 2")

    #     elif imc >=40:
    #         print(f"o valor do IMC é: {imc:.2f} - Voce esta com OBESIDADE MORBITA")

    #     else:
    #         print("ACIMA")  


    # except Exception as e:
    #     print(f"Vc não tem idade para assistir esse filme.{e}")    
    #     continue
