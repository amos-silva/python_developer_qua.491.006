""" programa que com as operações:
    Cadastre novo nome da lista
    Liste todos os nomes
    Pesquise por um nome
    Altere um nome
    Exclua um nome
    Sair do programa
    a lista deve iniciar vazia lista = []

    os.system("cls" if os.name == "nt" else "clear")
"""
import os

nomes = []  #lista vazia

while True: #MENU

    print(" -------- MENU -------- ")
    print("1 - Cadastrar novo nome")
    print("2 - Listar os nomes")
    print("3 - Pesquisar nomes")
    print("4 - Alterar um nome")
    print("5 - Excluir um nome")
    print("6 - SAIR")

    opcao = input("Informe a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                novo_nome = input(">>> Inserir Novo Nome: ").title().strip()
                nomes.append(novo_nome)     #append - inserir novo nome
                print(f"{novo_nome} inserido com sucesso!")
            except Exception as e:
             print(f"Não foi possivel Executar. {e}")
            finally:
                continue
              
        case "2":
            try:
                for i in range(len(nomes)):     
                    print(f"Indice: {i}: {nomes[i]}")
                    #print('-'*20)
            except Exception as e:
             print(f"Não foi possivel Exibir. {e}")
            finally:
                continue

        case "3":
            pesquisa = input("Informe o nome da pesquisa: ").title().strip()
            os.system("cls" if os.name == "nt" else "clear")
            qtde = nomes.count(pesquisa)
            print(f"{pesquisa} Foi encontrado {qtde} vezes na lista")
            continue

        case "4":
            try:
                for i in range(len(nomes)):              #imprimir a lista
                    print(f"Indice: {i}: {nomes[i]}")
                indice = int(input("Informe o INDICE a ser ALTERADO: "))
                if indice >=0 and indice < len(nomes):
                    nomes[indice] = input("informe o novo nome: ").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print("nome alterado com sucesso !")

                    for i in range(len(nomes)):          #imprimir novamente a lista
                        print(f"Indice: {i}: {nomes[i]}")
                else:
                    print("Indice inválido")
            except Exception as e:
                print(f"Não foi possivel ALTERAR. {e}")
            finally:
                continue

        case "5":
            try:
                for i in range(len(nomes)):              #imprimir a lista
                    print(f"Indice: {i}: {nomes[i]}")
                indice = int(input("informe a posição para excluir: "))
                if indice >=0 and indice < len(nomes):
                    del(nomes[indice])
                    print("Nome excluido com sucesso !")
                    for i in range(len(nomes)):              #imprimir a lista
                        print(f"Indice: {i}: {nomes[i]}")
                else:
                    print("Posição inválida !")
                    
            except Exception as e:
             print(f"Não foi possivel DELETAR. {e}")
            finally:
                continue
            