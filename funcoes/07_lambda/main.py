import os
"""
# Função normal
def somar(x, y):
    result = x+y
    return result
"""

# FUNÇÃO LAMBDA
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
somar = lambda x, y: x+y

#algoritimo principal
if __name__ == "__main__":
    try:
        x = int(input("Valor de X: "))
        y = int(input("Valor de Y: "))
        result = somar(x, y)

        limpar()
        print(f"O Total da Soma é: {result}")

    except Exception as e:
        print(f"Erro ao somar. {e}")
