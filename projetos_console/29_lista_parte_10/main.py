# concatenar uma lista em uma variavel

dias_semana = ["Domingo", "Segunda", "Terça", 
               "Quarta", "Quinta", "Sexta", "Sábado"]

delimitador = ", "  # para separar os valores
dias_variavel = delimitador.join(dias_semana)   #join para juntar todos os nomes

print(dias_variavel)