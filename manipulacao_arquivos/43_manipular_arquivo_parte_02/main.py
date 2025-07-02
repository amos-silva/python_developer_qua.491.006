import os

while True:
    try:
        arquivo = input("Informe o NOME do arquivo: ").strip().lower()

        with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:    #LEITURA E ABERTURA DO ARQUIVO
            arquivo_aberto = f.read()

            print(arquivo_aberto)
        while True:                 #while para abrir opções para usuario
            prosseguir = input("Deseja abrir outro ? S / N : ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção invalida")
                
        match prosseguir:
            case "s":
                continue
            case "n":
                break
    except Exception as e:
        print(f"Não foi possivel ler")
        continue