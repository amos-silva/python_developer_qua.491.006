import json    # para trabalhar com arquivos Json , precisa importar sempre essa biblioteca

try:
    arquivo = input("informe o nome do arquivo: ").strip().lower()

    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:   #ler o arquivo e converte em um dicionario
        dados = json.load(f)    # carrega o arquivo json
    
    print(f"{'-'*20} DADOS {'-'*20}")
    for dado in dados:
        for chave in dado:
            print(f"{chave.capitalize()}: {dado.get(chave)}")
        print(f"{'-'*40}\n")

except Exception as e:
    print(f"Não foi possivel ler o arquivo JSON. {e}")