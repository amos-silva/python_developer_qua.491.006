import datetime
from datetime import date

hoje = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Data da exucução do programa: {hoje} - Hora da Execução: {hora}")
