#lista - inserir novo item na lista
nomes = [
    "Amós",
    "Joana",
    "João",
    "Mariana",
    "Mário",
    "Fernanda"
]
for nome in nomes:
    print(nome)

# variavel para inserir novo nome
novo = input(">>> Inserir Novo Nome: ").title().strip() #title para colocar  a primeira letra em caixa alta - strip, para ognorar digitos invalidos

nomes.append(novo)  #   append, para inserir novo nome

for nome in nomes:  # imprimir nova lista
    print(nome)
