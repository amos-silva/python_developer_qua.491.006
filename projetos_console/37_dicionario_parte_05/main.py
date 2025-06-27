#Dicinario - ADICIONAR NOVA CHAVE AO DICIONARIO
usuario = {
    'nome':"Amós da Silva",
    'idade': 39,
    'email': "amos@hotmail.com"
}
for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")

#ADICIONAR NOVA CHAVE AO DICIONARIO

usuario['profissao'] = input("Informe a Profissão: ").strip()

print("----------------------------")
for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
