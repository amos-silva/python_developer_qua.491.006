#   importar biblioteca
import os   #biblioteca do sistema operacional

while True:
    nome = input("Informe seu nome: ")
    os.system("cls")
    print(f"Seja bem vindo, {nome}")
  

    opcao = input("Deseja continuar?    S / N ").lower().strip()

    match opcao:
        case "s":
            os.system("cls")
            continue
        case "n":
            break
        case _:
            print("Opção invalida")
            break
        