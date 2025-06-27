#Dicinario - uma lista que é separada por valor/chave/nome, e não por numero/posição - usa-se {}
usuario = {
    'nome':"Amós da Silva",
    'idade': 39,
    'email': "amos@hotmail.com",
    'profissao': "Técnico em Ti"
}

print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"Profissão: {usuario.get('profissao')}")
print(f"Teste: {usuario.get('teste')}")   # usando o .get ele não da erro no sistema, simplismente retorna vazio
