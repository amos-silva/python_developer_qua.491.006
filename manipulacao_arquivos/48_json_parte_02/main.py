import json
import os
    # adicionar mais uma pessoa ao arquivo
pessoa = {}     #dicionario vazio

try:
    arquivo = input("Informe o arquivo: ").strip().lower()
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
    
    #informar os dados da nova pessoa
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe o idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['data_nasc'] = input("Informe o D/N: ").strip()
    pessoa['sexo'] = input("Informe o Genero: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe o nome da Mãe: ").strip().title()
    pessoa['pai'] = input("Informe o nome do Pai: ").strip().title()
    pessoa['email'] = input("Informe o Email: ").strip().lower()
    pessoa['senha'] = input("Informe a Senha: ")
    pessoa['cep'] = input("Informe o CEP: ").strip()
    pessoa['endereco'] = input("Informe o Endereço: ").strip().title()
    pessoa['numero'] = int(input("Informe o Numero: "))
    pessoa['bairro'] = input("Informe o Bairro: ").capitalize().strip()
    pessoa['cidade'] = input("Informe a Cidade: ").strip().title()
    pessoa['estado'] = input("Informe o Estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o Telefone: ").strip()
    pessoa['celular'] = input("Informe o Celular: ").strip()
    pessoa['altura'] = float(input("Informe o Altura: ").replace(",", "."))
    pessoa['peso'] = float(input("Informe o Peso: ").replace(",", "."))
    pessoa['tipo_sanguineo'] = input("Informe o Tipo Sanguineo: ").strip().capitalize()
    pessoa['cor'] = input("Informe a Cor: ").strip()

    pessoas.append(pessoa)  #adicionar o dicionario pessoa à lista pessoas

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:   #granando no arquivo
        json.dump(pessoas,f, ensure_ascii=False, indent=4)

    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
    
    print(f"{'-*20'} LISTA ATUALIZADA {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print(f"{'-*40'}")

except Exception as e:
    print(f"Não foi possivel inserir. {e}")