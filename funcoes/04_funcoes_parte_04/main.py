# IMPORTAR PARTE DO ARQUIVO MODULO - Somente as funções necessárias
from modulo import limpar_tela, vel_media, acel_media

# PROGRAMA PRINCIPAL
if __name__ == "__main__":  # BLOQUEAR PARA QUE O MAIN NÃO SEJA IMPORTADO PARA OUTRO ARQUIVO.

    v = 0

    while True:
        print("1 - Calcular VELOCIDADE Média.")
        print("2 - Calcular TEMPO Médio.")
        print("3 - SAIR.")
        opcao = input("Informe a opção: ").strip()
        limpar_tela()

        match opcao:
            case "1":
                try:
                    vi = float(input("Velocidade INICIAL: ").replace(",", "."))
                    vf = float(input("Velocidade FINAL: ").replace(",", "."))
                    v = vel_media(vi, vf)

                    print(f"Velocidade MEDIA: {v}")

                except Exception as e:
                    print(f"ERRO. {e}")
                finally:
                    continue

            case "2":
                try:
                    t = float(input("Informe o TEMPO: ").replace(",", "."))

                    if v != 0:
                        a = acel_media(v, t)
                        print(f"Aceleração MEDIA: {a}")

                    else:
                        print("Sem velocidade media - Retorne")

                except Exception as e:
                    print(f"ERRO. {e}")
                finally:
                    continue          

            case "3":
                print("SAIU !!!")
                break
            case _:
                print("Opção inválida")
                continue