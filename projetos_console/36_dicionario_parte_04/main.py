#Dicinario - forma ALTERNATIVA
usuario = dict(nome="Amós", idade=39, email="amos@hotmail.com", profissao="Ti")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")    #capitalize para Caixa Alta
