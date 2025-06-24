#lista - Alterar um item na lista
itens = [
    "Chocolate",
    "Frango",
    "Carne",
    "Arroz",
    "Feijão",
    "Leite",
    "Ovos",
]

for i in range(len(itens)):     # Exibe a lista
    print(f"Indice: {i}: {itens[i]}")

try:    #Alterar o intem atravez do indice
    i = int(input("Informe a posição da lista que deseja alterar: "))

    if i>=0 and i <len(itens):  # verificar se existe o item
        itens[i] = input("Informe o novo nome: ").capitalize().strip()
        print("Item alterado com sucesso!")
    else:
        print("Intem inválido <<<\n")

except Exception as e:
    print(f"Não foi possivel alterar. {e}")
finally:    # reimprimir a lista com novo valor alterado
    for i in range(len(itens)):
        print(f"Indice {i}: {itens[i]}")