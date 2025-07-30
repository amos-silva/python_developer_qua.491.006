import modulo as mo

if __name__ == "__main__":  # BLOQUEAR PARA QUE O MAIN NÃO SEJA IMPORTADO PARA OUTRO ARQUIVO.
    while True:
        print("1 - Calcular Equação 1º Grau.")
        print("2 - Calcular Equação 2º Grau.")
        print("3 - SAIR.")
        opcao = input("informe a opção: ").strip()
        mo.limpar_tela()

        match opcao:
            case "1":
                try:
                    a = float(input("Informe o valor de A: ").replace(",", "."))
                    b = float(input("Informe o valor de B: ").replace(",", "."))
                    x = mo.primeiro_grau(a, b)
                    print(f"o valor de X é: {x} ")

                except Exception as e:
                    print(f"Erro. {e}")
                finally:
                    continue

            case "2":
                try:
                    a = float(input("Informe o valor de A: ").replace(",", "."))
                    b = float(input("Informe o valor de B: ").replace(",", "."))
                    c = float(input("Informe o valor de C: ").replace(",", "."))
                    x = mo.segundo_grau(a, b, c)
                    for result in x:
                        print(f"{result}")

                except Exception as e:
                    print(f"Erro. {e}")
                finally:
                    continue

            case "3":
                print("SAIU ... ")
                break
            case _:
                print("ERRO! ")
                continue