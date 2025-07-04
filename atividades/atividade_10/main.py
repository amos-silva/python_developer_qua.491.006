"""
Faça um CRUD (Create, Read, Update, Delete) em um JSON.
opções do MENU:
1-Criar novo Arquivo JSON (Informar o caminho que deseja criar)
2-Abrir arquivo JSON (Informar o caminho para abrir)
3-Cadastrar novo usuario
4-Listar todos usuarios
5-Pesquisar um usuario (pelo valor da chave)
6-Alterar dados de um usuario
7-Deletar usuario
8-Sair

DADOS DO USUARIO:
Nome
D/N
CPF
Email
Telefone
Filme Favorito
"""

import json
import os

lista = []       # lista vazia

while True:         #Laço de repetição
    usuario = {}    #dicionario vaizio
    novo_arquivo = ""
    diretorio = ""

    print(f"{'-'*20} {diretorio} MENU {novo_arquivo} {'-'*20}") 

    print("1 - Criar novo Arquivo JSON: (Informe o caminho)")
    print("2 - Abrir arquivo JSON: (Informe o caminho)")
    print("3 - Cadastrar novo usuario: ")
    print("4 - Listar todos usuarios ")
    print("5 - Pesquisar um usuario: ")
    print("6 - Alterar dados de um usuario: ")
    print("7 - Deletar usuario: ")
    print("8 - SAIR ")
    opcao = input("Informe a opção: ")
    os.system("cls" if os.name =="nt" else "clear")
    
    match opcao:    # match case = OPÇÕES
        case "1":
            if not novo_arquivo:    # veririficar se existe o arquivo e se esta cheio ou vazio
                novo_arquivo = input("Informe o nome do Arquivo: ").strip().lower()
                diretorio = input("Informe o Diretório para Salvar: ").strip().lower()
                with open(f"{novo_arquivo}.json", "w", encoding="utf-8") as f:     #abrir arquivo e alterar
                    json.dump(lista, f, ensure_ascii=False, indent=4)               #".dump" = Criar novo arquivo e Salvar
                os.system("cls" if os.name =="nt" else "clear")
                print("Arquivo SALVO")
            continue

        case "2":
            novo_arquivo = input("Informe o nome do Arquivo: ").strip().lower()
            diretorio = input("Informe o caminho do Diretório: ").strip().lower()
            with open(f"{novo_arquivo}.json", "r", encoding="utf-8") as f: #abrir arquivo e alterar
                json.dump(lista, f, ensure_ascii=False, indent=4)            #".dump" = Criar novo arquivo e Salvar
                os.system("cls" if os.name =="nt" else "clear")
                print("Arquivo Aberto")
                continue

        case "3":
            usuario['nome'] = input("Informe o Nome: ").strip().title()
            usuario['dn'] = input("Informe a D / N: ")
            usuario['cpf'] = input("Informe o CPF: ")
            usuario['email'] = input("Informe o email: ").strip().title()
            usuario['tel'] = input("Informe o Telefone: ")
            usuario['filme'] = input("Informe o Filme: ").strip().lower()

            lista.append(usuario)    #inserir o dicionario "usuario" dentro da lista "usuarios"
            os.system("cls" if os.name =="nt" else "clear")
            print("Usuario Cadastrado")
            continue

            ...

        case "4":
            if not novo_arquivo:    # veririficar se existe o arquivo e se esta cheio ou vazio
                novo_arquivo = input("Informe o nome do Arquivo: ").strip().lower()
         
            with open(f"{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)    #carregar o arquivo
            print(f"{'-'*20} USUARIOS {'-'*20}") 
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print('-'*40)
            continue       

        case "5":
            
            print("Pesquisa de usuario")
            continue

        case "6":
                
            print("Alterar Usuario")
            continue

        case "7":
            
            print("Deletar usuario")
            continue

        case "8":
            print("PROGRAMA ENCERRADO")
            break  

        case _:
            print("Opção invalida")
            continue