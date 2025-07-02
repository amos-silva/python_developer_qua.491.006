import os

while True:
    try:
        novo_texto = input("Digite um texto: \n")
        nome_arquivo = input("Nome do Arquivo - SEM A EXTENSÃO : ").strip().lower()
        with open(f"44_manipular_arquivo_parte_03/{nome_arquivo}.txt", "w", encoding="utf-8") as f:     #Salvar dentro da parta 44
            f.write(novo_texto)
        print(f"{nome_arquivo}.txt Gravado com Sucesso.")
        os.system("cls" if os.name=="nt" else "clear")
        
        while True:                 #while para abrir opções para usuario
            prosseguir = input("Deseja CRIAR NOVO ARQUIVO ? S / N : ").strip().lower()
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
        print(f"Erro ao gravar arquivo.{e}")
