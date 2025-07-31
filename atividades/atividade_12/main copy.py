### calcular área e cricunferencia de um circulo - usando LAMBDA
import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            r = float(input("Informe o Raio do circulo: ").replace(",", "."))

            print(f"A Area é: {mo.area(r):.2f}  >>>  A Circunferencia é: {mo.circ(r):.2f}")

        except Exception as e:
            print("ERRO, {e}")