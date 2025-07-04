import json
import os

usuarios = []       # lista vazia

while True:         #Laço de repetição
    usuario = {}    #dicionario vaizio

    print("1 - Cadastrar novo Usuario: ")
    print("2 - Salvar Arquivo JSON: ")
    print("3 - Ler Arquivo JSON: ")
    print("4 - SAIR ")
    opcao = input("Informe a opção: ")
    os.system("cls" if os.name =="nt" else "clear")

    novo_arquivo = ""
    match opcao:    # match case = OPÇÕES
        case "1":
            usuario['nome'] = input("Informe o Nome: ").strip().title()
            usuario['idade'] = int(input("Informe a Idade: "))
            usuario['email'] = input("Informe o Email: ").strip().lower()

            usuarios.append(usuario)    #inserir o dicionario "usuario" dentro da lista "usuarios"
            os.system("cls" if os.name =="nt" else "clear")
            print("Usuario Cadastrado")
            continue

        case "2":
            novo_arquivo = input("Informe o nome do Arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding="utf-8") as f: #abrir arquivo e alterar
                json.dump(usuarios, f, ensure_ascii=False, indent=4)            #".dump" = Criar novo arquivo e Salvar
                os.system("cls" if os.name =="nt" else "clear")
                print("Arquivo SALVO")
                continue

        case "3":
            if not novo_arquivo:    # veririficar se existe o arquivo e se esta cheio ou vazio
                novo_arquivo = input("Informe o nome do Arquivo: ").strip().lower()
         
            with open(f"50_json_parte_04/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)    #carregar o arquivo
            print(f"{'-'*20} USUARIOS {'-'*20}") 
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print('-'*20)
                continue

        case "4":
            print("PROGRAMA ENCERRADO")
            break        

        case _:
            print("Opção invalida")
            continue