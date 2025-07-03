import json
import os

# converter chaves - string em float

try:
    arquivo = input("Informe o arquivo que deseja converter: ").strip().lower()
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:   #ler o arquivo original
        lista = json.load(f)        # load carrega o arquivo

    for dado in lista:  # converção do tipo de arquivo
        dado['altura'] = dado['altura'].replace(",", ".")   #replace para alterar , em .
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])

    #converter um json e grava o arquivo correto
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista,f, ensure_ascii=False, indent=4)

    print("Conversão realizada")
    
except Exception as e:
    print(f"Não foi possivel converter. {e}")