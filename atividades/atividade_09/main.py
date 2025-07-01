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
# bibliotecas
import os
import random
import datetime
from datetime import date

# lista vazia
usuarios = []

# loop
while True:
    # dicionário
    usuario = {}

    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Alterar dados de um usuário")
    print("4 - Sortear usuário")
    print("5 - Excluir usuário")
    print("6 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    # limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

    # verifica a opção do usuário
    match opcao:
        case "1":
            try:
                usuario['nome'] = input("Informe o nome: ").strip().title()
                usuario['data de nascimento'] = input("Informe a data de nascimento: ").strip()
                usuario['email'] = input("Informe o email: ").strip().lower()
                usuario['cpf'] = input("Informe o CPF: ").strip()
                usuario['telefone'] = input("Informe o telefone: ").strip()
                usuario['genero'] = input("Informe o gênero: ").strip()
                usuario['data do cadastro'] = date.today().strftime("%d/%m/%Y")
                usuario['hora do cadastro'] = datetime.datetime.now().strftime("%H:%M:%S")

                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")

                print(f"Usuário {usuario.get('nome')} cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possível cadastrar usuário. {e}.")
            finally:
                continue
        case "2":
            try:
                for i in range(len(usuarios)):
                    print(f"Índice: {i}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    print('-'*40)
            except Exception as e:
                print(f"Não foi possível listar usuários. {e}.")
            finally:
                continue
        case "3":
            try:
                i = int(input("Informe o índice que deseja alterar: "))
                os.system("cls" if os.name == "nt" else "clear")
                if i >= 0 and i < len(usuarios):
                    print(f"{'-'*20} Dados do usuário {'-'*20}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    print("\n")
                    while True:
                        chave_escolhida = input("Informe a chave a alterar:").strip().lower()
                        if chave_escolhida in usuarios[i]:
                            usuarios[i][chave_escolhida] = input(f"Informe o novo valor de {chave_escolhida}: ")
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Chave alterada com sucesso.")
                        else:
                            print("Chave inexistente.")
                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir == "s" or prosseguir == "n":
                                break
                            else:
                                continue
                        match prosseguir:
                            case "s":
                                continue
                            case "n":
                                break
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar dados. {e}.")
            finally:
                continue
        case "4":
            try:
                i = random.randint(0, len(usuarios)-1)
                print("Usuário sorteado:")
                for chave in usuarios[i]:
                    print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
            except Exception as e:
                print(f"Não foi possível sortear usuário. {e}.")
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe o índice a ser excluído: "))
                if i >= 0 and i < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    while True:
                        excluir = input("Tem certeza? (s/n): ").strip().lower()
                        if excluir == "s" or excluir == "n":
                            break
                        else:
                            print("Opção inválida.")
                            continue
                    match excluir:
                        case "s":
                            del usuarios[i]
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário excluído com sucesso.")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário não excluído.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir usuário. {e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue