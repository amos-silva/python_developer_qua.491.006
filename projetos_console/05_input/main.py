# input - ENTRADA DE DADOS
nome = input("Informe seu nome: ")
idade = int(input("Informe sua Idade: "))
altura = float(input("Informe sua Altura: ").replace(",", ".")) # REPLACE SUBSTITUI CARACTER

# Saida de Dados
print(f"Seja bem vindo ao curso de Python, {nome}")
print(f"{nome}: {type(nome)}")
print(f"Idade do Usuário: {idade}")
print(f"{idade}: {type(idade)}")
print(f"Informe sua Altura: {altura}")
print(f"{altura}: {type(altura)}")
