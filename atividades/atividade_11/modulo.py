# receber um numero inteiro e o programa calcula o valor da sequancia de Fibonacci
def fibonacci(n):
 
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
