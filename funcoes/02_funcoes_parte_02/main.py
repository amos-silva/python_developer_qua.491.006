#FUNÇÃO
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"


# PROGRAMA PRINCIPAL
nome = input("Informe seu nome: ").strip().title()
print(mostrar_msg(nome))