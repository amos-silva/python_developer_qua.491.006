# extrair um nome da lista e colocar em uma variavel
import os

nomes = ["Fulano", "Amós", "Camila", "Bianca", "Ruy", "José"]
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")

try:
    indice = int(input("Informe a posição do indice que deseja: "))
    if indice >=0 and indice < len(nomes):
        nome_isolado = nomes.pop(indice)    #pop para extrair
        os.system("cls" if os.name=="nt" else "clear")
        print(f"{nome_isolado}, separado com sucesso!")

        # exibe a lista sem o item isolado
        for indice in range(len(nomes)):
            print(f"{indice}: {nomes[indice]}")
        
        # exibe o item isolado
        print(f"Valor isolado da lista: {nome_isolado}")

    else:
        print("Indice invalido")

except Exception as e:
    print(f"Não foi possivel executar. {e}")