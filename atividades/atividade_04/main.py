import os
import time
import datetime
from datetime import date

hoje = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Hora da Execução: {hora}")

while True:
    hora == hora
    os.system("cls")
    print(f"{hora}")
    time.sleep(1)