#Lista, variavel que pode receber varios valores aleatorios na mesma variavel
nomes = ["Fulano", "Cicrano", "Beltrano", "Amós", "Teste", "777" ]
print(nomes)    # imprime todos da lista
print("-------------------------")
print(nomes[0]) #impreme a posicao 0 que é o primeiro nome, porque a posicao Zero tambem é contada
print("-------------------------")
print(nomes[3]) #impreme a posicao 3 que é o quarto nome, porque a posicao Zero tambem é contada
print("-------------------------")

print(len(nomes))           # conta o numero de itens de uma lista
print("-------------------------")

nomes.sort()               # Ordem crescente

#nomes.sort(reverse=True)    #Ordem decrescente

for nome in nomes:  # for , usado par alaço de repetição.
    print(nome)
