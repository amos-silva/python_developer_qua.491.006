"""
criar programa que façaas seguintes funções:
#cadastre um novo usuario
#liste todos usuarios
#altere dados de um usuario
#fazer sorteio de usuario
#exlua um usuario
#saia do programa
## Dados do usuario: Nome completo, DN, email, CPF, Tel, Genero, Data do cadastro, Hora do cadastro
"""
import os
import random
import datetime
from datetime import date

lista = []      #Lista Vazia

data = date.today().strftime("%d/%m/%Y") #converter data para Brasil
hora = datetime.datetime.now().strftime("%H:%M:%S") #converter hora para Brasil

while True: #MENU
    usuario = {}        #Dicionario Vazio

    print(" ------------------ MENU ------------------ ")
    print("1 - Cadastrar novo Usuário")
    print("2 - Listar Usuários")
    print("3 - Alterar um Dados")
    print("4 - Sortear Usuário")
    print("5 - Excluir um Usuário")
    print("6 - SAIR")
    print(" ------------------------------------------ ")

    opcao = input("Informe a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")    #capitalize para Caixa Alta

                usuario['nome'] = input("Informe o Nome: ").title().strip()
                usuario['dn'] = input("Informe a Data de Nascimento: ").title().strip()
                usuario['email'] = input("Informe Email: ").title().strip()
                usuario['cpf'] = (input("Informe o CPF: ")).title().strip()
                usuario['tel'] = (input("Informe o Telefone: ")).title().strip()
                usuario['genero'] = input("Informe o Genero: ").title().strip()
                usuario['data'] = print(f"Data: {data}")
                usuario['hora'] = print(f"Hora: {hora}")

                lista.append(usuario)   #Adicionar dicionario dentro da lista
          
                print("Usuário cadastrado com sucesso! \n")

            except Exception as e:
             print(f"Não foi possivel Cadastrar. {e}")
            finally:
                continue
           
        case "2":
            try:
                print(" --------------LISTA DE USUÁRIOS------------------- ")
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(lista)}")    #capitalize para Caixa Alta
                    for usuario in lista:
                        print(f"{lista.capitalize()}: {usuario.get(usuario)}")  

            except Exception as e:
                print(f"Não foi possivel Exibir. {e}")
            finally:
                continue

        case "3":
            try:
                for chave in usuario:
                    print(f"{chave}: {usuario.get(chave)}")
                
                    #ALTERAR UMA CHAVE DO DICIONARIO - Informe a chave :
                    chave = input("Informe a chave para alterar: ").lower().strip()

                    if chave in usuario:        #Verificar se existe a chave
                        usuario[chave] = input(f"Informe o novo valor: {chave}: ").strip()
                        print("---------- DADOS ALTERADOS ------------")
                    else:
                        print("Valor inexistente")
                    for chave in usuario:
                        print(f"{chave}: {usuario.get(chave)}")
                        
            except Exception as e:
                print(f"Não foi possivel ALTERAR. {e}")
            finally:
                continue

        case "4":
            try:                
                i = random.randint(0, len(lista)-1)   #conta a lista, 0 é o primeiro e len conta o tamanho da lista
                print(f"Nome sorteado: {lista[i]}")
                continue
                    
            except Exception as e:
                print(f"Erro ao Sortear. {e}")
            finally:
                continue

        case "5":
            try:
                for chave in usuario:
                    print(f"{chave}: {usuario.get(chave)}")
                    print("----------------------------")

                #DELETAR UMA CHAVE DO DICIONARIO - Informe a chave :
                chave = input("Informe a chave para DELETAR: ").lower().strip()

                if chave in usuario:        #Verificar se existe a chave
                    del usuario[chave]
                    print("----------USUÁRIO DELETADO------------")
                else:
                    print("Chave inexistente")                
                    
            except Exception as e:
                print(f"Não foi possivel DELETAR. {e}")
            finally:
                continue

        case "6":
            print(" VC SAIU ")
            break
