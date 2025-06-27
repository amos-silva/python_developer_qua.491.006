#Dicinario - ATEARAR DADOS NO DICIONARIO
usuario = {
    'nome':"Amós da Silva",
    'idade': 39,
    'email': "amos@hotmail.com",
    'profissao': "Técnico em Ti"
}

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
print("----------------------------")

#ALTERAR UMA CHAVE DO DICIONARIO - Informe a chave :
chave = input("Informe a chave para alterar: ").lower().strip()

if chave in usuario:        #Verificar se existe a chave
    usuario[chave] = input(f"Informe o novo valor: {chave}: ").strip()
    print("----------VALORES ALTERADOS------------")
else:
    print("Valor inexistente")
for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
