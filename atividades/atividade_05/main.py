""" criar programa com nome e idade. depois mostre os filmes e indicações de idade.
o usuario vai esoclher a sala, se tiver idade para assistir, o programa exibe os dados, o filme, a data e hora no bilhete.
senão, ele volta e escolhe outra sala com filme adequado."""

import os
import datetime
from datetime import date

dia = date.today().strftime("%d/%m/%Y") #converter data para Brasil
hora = datetime.datetime.now().strftime("%H:%M:%S") #converter hora para Brasil

#Salas
sala1 = "A Roda Quadrada"
sala2 = "A Volta dos que não Foram"
sala3 = "Poeira em Alto Mar"
sala4 = "As Tranças do Rei Careca"
sala5 = "A Vingança do Peixe Frito"


while True:
    try:  
        nome = input("Informe seu nome: ").title().strip()
        idade = int(input("Sua idade: "))

        while True:
            print("----- MENU DE FILMES ----- \n")
            print(f"Sala-1 - {sala1} - Livre")
            print(f"Sala-2 - {sala2} - Livre")
            print(f"Sala-3 - {sala3} - Livre")
            print(f"Sala-4 - {sala4} - Livre")
            print(f"Sala-5 - {sala5} - Livre")

            sala = input("Informe a Sala: ").strip()
            os.system("cls" if os.name == "nt" else "clear")

            match sala:
                case "1":
                    idade_minima = 0
                    filme = sala1
                case "2":
                    idade_minima = 12
                    filme = sala2
                case "3":
                    idade_minima = 14
                    filme = sala3
                case "4":
                    idade_minima = 16
                    filme = sala4
                case "5":
                    idade_minima = 18
                    filme = sala5
                case _:
                    print("Digite uma sala de 1 a 5")
                    continue
            if idade >= idade_minima:
                print(f"filme: {filme}  - Idade minima:  {idade_minima}")
                print(f"Ingresso comprado por: {nome}, no dia: {dia} às {hora}.")
                print(f"🎞️🎆 Tenha um Bom filme ")
           
                break
            else:
                print(f"{nome}, Voce nao tem idade para ver esse filme, Procure outro filme")

    except Exception as e:
        print(f"Não foi possivel comprar o ingresso.{e}")