import os

try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:    #ABRE O ARQUIVO
        texto = f.read()
    print(texto)

    novo_texto = input("Digite novo Texto: \n")

    with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:    #ABRE E EDITA O ARQUIVO
        f.write(novo_texto)

except Exception as e:
    print(f"Erro ao atualizar. {e}")