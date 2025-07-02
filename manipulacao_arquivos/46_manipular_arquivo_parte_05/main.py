import os

try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:    #ABRE O ARQUIVO
        texto = f.read()
    print(f"Texto existente: \n {texto}")

    novo_texto = input("Digite novo Texto: \n")
    nova_gravacao = f"{texto}\n{novo_texto}"
    
    with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:    #ABRE E EDITA O MESMO ARQUIVO
        f.write(nova_gravacao)
    print("Atualização do arquivo OK")

    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:    #ABRE O ARQUIVO JÁ ATUALIZADO
        texto_final = f.read()
    print(f"Texto atualizado: \n {texto_final}")

except Exception as e:
    print(f"Erro ao atualizar. {e}")