#programa de SORTEIO
import os
import random

nomes = []

while True:
    print("----- MENU -----")
    print("1 - INSERIR nome na lista")
    print("2 - EXIBIR nomes")
    print("3 - SORTEAR")
    print("4 - SAIR")
    print("-----------------------")

    opcao = input("informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                novo_nome = input("informe o nome: ").title().strip()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome)
                print(f"{novo_nome}, nome inserido com sucesso! \n")

                nomes.sort()    #coloca em ordem alfabetica
                for nome in nomes:
                    print(nome)      
                                
            except Exception as e:
                print(f"Erro ao inserir. {e}")
            finally:
                continue

        case "2":
            try:
                nomes.sort()    #coloca em ordem alfabetica
                for nome in nomes:
                    print(nome)      
                         
            except Exception as e:
                print(f"Erro ao pesquisar. {e}")
            finally:
                continue

        case "3":
            i = random.randint(0, len(nomes)-1)   #conta a lista, 0 é o primeiro e len conta o tamanho da lista
            print(f"Nome sorteado: {nomes[i]}")
            continue

        case "4":
            print("Programa Encerrado")
            break

        case _:
            print("Opção invalida")
            continue