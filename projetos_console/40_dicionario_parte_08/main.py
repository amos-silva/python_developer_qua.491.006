#Dicinario
chaves = ("Nome", "idade", "email", "Telefone", "Profissao")    #usando tupla para não apagar a chave do dicionario

usuario = {
    chaves[0]: "Amós",
    chaves[1]: "39",
    chaves[2]: "amos@amos",
    chaves[3]: "61-9999-8888",
    chaves[4]: "Ti"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")