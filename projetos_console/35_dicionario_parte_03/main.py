#Dicinario - uma lista que é separada por valor/chave/nome, e não por numero/posição - usa-se {}
usuario = {
    'nome':"Amós da Silva",
    'idade': 39,
    'email': "amos@hotmail.com",
    'profissao': "Técnico em Ti"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")    #capitalize para Caixa Alta
