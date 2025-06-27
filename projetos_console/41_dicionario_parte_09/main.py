#Dicinario - dentro da lista tem um dicionario, para usuario não excluir a chave,
#                                                  mas apenas o valor da chave.
usuarios= [
{
    'nome': "Amós",
    'idade': 39,
    'email': "amos@amos"
},
{
    'nome': "Camila",
    'idade': 41,
    'email': "camila@amos"
},
{
    'nome': "Bianca",
    'idade': 16,
    'email': "bianca@amos"
}
]

for usuario in usuarios:
    print('-'*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")