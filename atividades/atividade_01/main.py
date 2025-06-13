"""
Criar programa que receba os valores de alcool e gasolina em reais.
e informe qual melhor combustivel para abastecer
O usuario pode repetir várias vezes e encerrar o programa quando desejar.
calculo: compensa etanol caso ele tenha até 70% do valor da gasolina. - seja 30% mais barato que a gasolina

"""
# Laço de Repetição - while True

while True:
    
        # Tratamento de Exceção - try / except
    try:
        gas = float(input("Informe valor da Gasolina: ").replace(",", "."))
        eta = float(input("Informe valor do Etanol: ").replace(",", "."))
        calc = eta/gas*100

        result = "Gasolina" if calc > 70 else "Etanol"      # ternario, opção simples para esolha sim ou não

        print(f"Calculo {calc:.2f} % da Gasolina")    # :. 2f  casas decimais no numero
        print(f"Compensa abastecer com {result}")

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
        continue
