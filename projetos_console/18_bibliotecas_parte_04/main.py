from datetime import date   # Importa apenas as fuções de data da biblioteca

dia = date.today().strftime("%d/%m/%Y") #converter data para Brasil
print(f"Data atual: {dia}")