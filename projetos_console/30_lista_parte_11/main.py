#separar os itens de uma varial, e montar uma lista
todos_meses = "Janeiro, Fevereiro, Março, Abril, maio, Junho,Julho, Agosto, Setembro, Outubro, Novembro, Dezembro"

# separando em uma lista
meses = todos_meses.split(", ")
for mes in meses:
    print(mes)