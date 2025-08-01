#lambda
pg = lambda x: x*2      # Progressão Geométrica de progressão 2
pa = lambda x: x+2      # Progressão Aritimética de progressão 2

# programa principal
if __name__ == "__main__":
    #lista
    numeros = [1,2,3,4,5,6,7,8,9]

    print(f"Progressão Aritimética: {list(map(pa,numeros))}")
    print(f"Progressão Geométrica: {list(map(pg,numeros))}")

