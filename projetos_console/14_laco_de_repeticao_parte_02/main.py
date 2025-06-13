# LOOP INFINITO  - WHILE TRUE
while True:
    print(f"{'-'*20} MENU {'-'*20} \n")  # menu
    print("0 para SAIR")
    print("1 para Somar")
    print("2 para Subtrair")
    print("3 para Multiplicar")
    print("4 para dividir")

    operador = input("informe a operação desejada: ").strip()   #strip para corrigir numero digitado

    match operador:
        case "0":
             print("Você encerrou")
             break       # breack para sair do loop
        case "1":
            try:
                x = float(input("Informe valor de X: ").replace(",", "."))
                y = float(input("Informe valor de Y: ").replace(",", "."))

                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                 print("Não foi possivel calcular. {e}")
            finally:
                continue    
        case "2":
            try:
                x = float(input("Informe valor de X: ").replace(",", "."))
                y = float(input("Informe valor de Y: ").replace(",", "."))

                print(f"{x} - {y} = {x-y}")
            except Exception as e:
                print("Não foi possivel calcular. {e}")
            finally:
                continue   
        case "3":
            try:
                x = float(input("Informe valor de X: ").replace(",", "."))
                y = float(input("Informe valor de Y: ").replace(",", "."))

                print(f"{x} X {y} = {x*y}")
            except Exception as e:
                print("Não foi possivel calcular. {e}")
            finally:
                continue   
        case "4":
            try:
                x = float(input("Informe valor de X: ").replace(",", "."))
                y = float(input("Informe valor de Y: ").replace(",", "."))

                print(f"{x} / {y} = {x/y}")
            except Exception as e:
                print("Não foi possivel calcular. {e}")
            finally:
                continue                    # para retornar ao inicio do loop
        case _:                             #   _:    Default
            print("Operador invalido")
            continue