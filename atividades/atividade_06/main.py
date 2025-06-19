"""programa que usuario informa o ano e o programa exibe todo o calendario do ano informado
ano a partir de 1900
usar biclioteca " calendar " """

import os
import calendar as c

try:
    while True:
        ano = int(input("Informe o ano: "))
        os.system("cls" if os.name == "nt" else "clear")
        if ano >= 1900:
            print(c.calendar(ano))
            while True:
                voltar = input("Deseja imprimir outro calendário? (s/n)").lower().strip()
                if voltar == "s" or voltar == "n":
                    break
                else:
                    print("Opção inválida.")
                    continue
            match voltar:
                case "s":
                    continue
                case "n":
                    break
        else:
            print("Calendário do ano não disponível.")
except Exception as e:
    print(f"Não foi possível imprimir o calendário. {e}")
