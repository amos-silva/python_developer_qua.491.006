#   contagem regressiva
import os
import time

try:

    num = int(input("Infornme um numero inteiro: "))

    while num>=0:
        os.system("cls")
        print(f"{num} ...")
        time.sleep(1)
        num-=1

except Exception as e:
    print(f"Não foi possivel executar. {e}")    
finally:
    os.system("cls")
    print("Boooommmmm !!!!!!")
    