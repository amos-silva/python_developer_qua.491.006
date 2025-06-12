# TRATAMENTO DE EXCEÇÃO  -  try e except
try:
    n = int(input("informe um numero INTEIRO: "))
    print(f" O Numero informado é: {n}")
except Exception as e:  # exception , variavel que vai mostrar qual erro foi gerado
    print(f" O Numero informado não é válido - {e}")
finally:    #comando para finalizar o programa
    print("O Programa foi finalizado!")
    