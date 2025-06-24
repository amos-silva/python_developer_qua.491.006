#lista - pesquisar um item na lista
cidades = [
    "df",
    "São Paulo",
    "Rio de janeiro",
    "Belo Horizonte",
    "Teresina",
    "Palmas"
    "Floripa",
    "Goiania",
    "Valparaiso",
    "Samambaia",
    "Taguatinga",
    "Ceilandia"
    "df",
    "Taguatinga",
    "df"
]
pesquisa = input("Informe o nome da cidade: ").strip()

qtde = cidades.count(pesquisa)  # contar quantas vezes aquele nome foi encontrado na lista

print(f"{pesquisa} Foi encontrado {qtde} vezes na lista")
