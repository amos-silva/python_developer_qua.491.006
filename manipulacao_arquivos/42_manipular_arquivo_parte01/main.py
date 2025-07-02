#Leitura de arquivo
with open("texto.txt", "r", encoding="utf-8") as f:   # "R" É para leitura encoding , linguagem do Brasil
    texto = f.read()

print(texto)