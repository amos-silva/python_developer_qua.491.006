#Dicinario - DELETAR DADOS NO DICIONARIO
usuario = {
    'nome':"Amós da Silva",
    'idade': 39,
    'email': "amos@hotmail.com",
    'profissao': "Técnico em Ti"
}

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
print("----------------------------")

#DELETAR UMA CHAVE DO DICIONARIO - Informe a chave :
chave = input("Informe a chave para DELETAR: ").lower().strip()

if chave in usuario:        #Verificar se existe a chave
    del usuario[chave]
    print("----------VALOR DELETADO------------")
else:
    print("Valor inexistente")
for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
