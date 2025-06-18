"""#   programa com MENU:
    calcular area de um circulo.
    calcular tamanho de uma circunferencia.
    sair do programa.
    para cada loop, o programa deve limpar o terminal.

"""
import os
import math as m

while True:     # looping
    print(" ----- MENU ----- ")
    print("1 - Calcular AREA do circulo")
    print("2 - Calcular CIRCUNFERENCIA")
    print("3 - Sair")

    opcao = input("Informe a opção: ").strip()

    os.system("cls" if os.name == "nt" else "clear")    # cls para windows e clear para outros OS

    try:
        if opcao =="1" or opcao == "2":
            raio = float(input("Informe o Raio: ").replace(",", ".")) 
        else:
            ... # ( ... ou pass serve para pular ou ignorar )
            os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                area = m.pi*raio**2                
                print(f"AREA do circulo: {area:.2f}")
                continue
            case "2":
                circ = 2*m.pi*raio
                print(f"CIRCUNFERENCIA do circulo: {circ:.2f}")
                continue
            case "3":
                print("VC saiu do programa")
                break
            case _:
                print("Opção invalida")
                continue

    except Exception as e:
        print("Não foi possivel calcular. {e}")
        continue
            
