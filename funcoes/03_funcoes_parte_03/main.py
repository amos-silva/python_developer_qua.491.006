# importar arquivo modulo, que contem as funções
import modulo as m  # chama o modulo e ( as )renomeia para ficar mais fácil

#ALGORITIMO PRINCIPAL
if __name__ == "__main__":  # BLOQUEAR PARA QUE O MAIN NÃO SEJA IMPORTADO PARA OUTRO ARQUIVO.
    while True:     # laço de repetição
        print("---------- MENU ----------") 
        print("1 - Calcular Quadrado.")        
        print("2 - Calcular Retangulo.") 
        print("3 - Calcular Triangulo.")        
        print("4 - SAIR.")

        opcao = input("Informe a opção Desejada: ").strip()
        m.limpar_tela()

        match opcao:
            case "1":
                try:
                    l = int(input("Informe o lado do Quadrado: "))
                    a = m.area_quadrado(l)
                    print(f"a Área do quadrado é: {a}")
                except Exception as e:
                    print(f"Erro {e}")
                finally:
                    continue
            case "2":
                try:
                    b = int(input("Informe a Base do Retangulo: "))
                    h = int(input("Informe a Altura do Retangulo: "))
                    a = m.area_retangulo(b, h)
                    print(f"a Área do RETANGULO é: {a}")
                except Exception as e:
                    print(f"Erro {e}")
                finally:
                    continue
            case "3":
                try:
                    b = int(input("Informe a Base do Triangulo: "))
                    h = int(input("Informe a Altura do Triangulo: "))
                    a = m.area_triangulo(b, h)
                    print(f"a Área do TRIANGULO é: {a} \n")
                except Exception as e:
                    print(f"Erro {e}")
                finally:
                    continue
            case "4":
                print("Programa encerrado")
                break            
            case _:
                print("Opção invalida")
                continue
