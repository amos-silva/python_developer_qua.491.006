### calcular área e cricunferencia de um circulo - usando LAMBDA
import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular Área do Circulo.")
            print("2 - Calcular Circunferencia do Circulo.")
            print("3 - SAIR.")                    
            opcao = input("Escolha: ").strip()

            match opcao:
                case "1":
                    r = float(input("Informe o Raio: ").replace(",", "."))
                    print(f"A Area do circulo é: {mo.area(r)}")
                
                case "2":
                    r = float(input("Informe o Raio: ").replace(",", "."))
                    print(f"A Circunferencia do circulo é: {mo.circ(r)}")

                case "3":
                    print("SAIU ! ")
                    break
                
                case _:
                    print("Opção invalida")
                    continue        
        except Exception as e:
            print("ERRO, {e}")
            continue