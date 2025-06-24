#lista - inserir novo item na lista em uma posição desejada
cidades = [
    "Brasília",
    "São Paulo",
    "Rio de janeiro",
    "Belo Horizonte",
    "Teresina",
    "Palmas"
]
for i in range(len(cidades)):   # for usando i range , para ler a quantidade e posição da lista
    print(f"Indice {i}: {cidades[i]}")

try:        # Tratamento de exceção, caso o usuario digite algo que não seja válido

    nova = input(">>> Informe a nova Cidade: ").title().strip()
    i = int(input("Informe a posição que deseja inserir: "))

    if i >=0 and i <= len(cidades):  # forçar o usuario a digitar um numero que eteja dentro da lista
        cidades.insert(i, nova) # inserir novo item na posição que desejo
        print("Cidade inserida com sucesso")

    else:
        print("Indice inválido")

except Exception as e:
    print(f"Não foi possivel, Não digitou um comando válido")
finally:
    #reexibir a nova lista
    for i in range(len(cidades)):
        print(f"Indice: {i}: {cidades[i]}")
