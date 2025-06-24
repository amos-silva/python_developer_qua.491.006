#lista - Deletar um item na lista
nomes = [
    "Amós",
    "Joana",
    "João",
    "Mariana",
    "Mário",
    "Mariana",
    "Bianca",
    "Camila",
    "Ruy"
]
for i in range(len(nomes)): #exibe a lista
    print(f"{i}: {nomes[i]}")

try:
    i = int(input("informe a posição para excluir: "))
    if i>=0 and i < len(nomes):
        del(nomes[i])
        print("Nome excluido com sucesso !")
    else:
        print("Posição inválida !")

except Exception as e:
    print(f"Não foi possivel excluir. {e}")
finally:
    for i in range(len(nomes)):
        print(f"{i}: {nomes[i]}")