"""#   programa com MENU:
    calcular area de um circulo.
    calcular tamanho de uma circunferencia.
    sair do programa.
    para cada loop, o programa deve limpar o terminal.

"""
import os
import math as m

while True:
    try:    

        raio = float(input("Informe o Raio do circulo: ").replace(",", "."))

        area = m.pi * raio**2
        circ = 2*m.pi*raio

        print(f"a AREA do circulo é: {area:.2f}")
        print(f"a CIRCUNFERENCIA do circulo é: {circ:.2f}")


        opcao = input("Novo calculo? S / N : ").lower().strip()    # louwer para digitos minusculos ou maisculos / strip para caracter invalido
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
    finally:
        os.system("cls")
