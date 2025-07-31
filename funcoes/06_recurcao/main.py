import modulo as mo
if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular Fatorial.")
            print("2 - SAIR.")                    
            opcao = input("Escolha: ").strip()

            match opcao:
                case "1":
                    n = int(input("Informe um numero INTEIRO: "))
                    print(f"Fatorial de: {n}! = {mo.fatorial(n)}")
                case "2":
                    print("SAIU ! ")
                    break
                case _:
                    print("Opção invalida")
                    continue        
        except Exception as e:
            print("ERRO, {e}")
            continue