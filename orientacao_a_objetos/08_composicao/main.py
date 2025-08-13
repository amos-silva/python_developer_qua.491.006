import classes as c

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")
    carro = c.Veiculo(modelo="", fabricante="", cor="", placa="", ano="", proprietario="")

    print("DADOS DO PROPRIETARIO")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o EMAIL: ").strip().lower()
    proprietario.telefone = input("Informe o Telefone: ").strip()
    proprietario.endereco = input("Informe o Endereço: ").strip().title()

    print("\nDADOS DO VEICULO")
    carro.fabricante = input("Informe a FABRICANTE: ").strip().title()
    carro.modelo = input("Informe o MODELO: ").strip().title()
    carro.cor = input("Informe a COR: ").strip().title()
    carro.placa = input("Informe a PLACA: ").strip().upper()
    carro.ano = input("Informe o ano: ").strip()
    carro.proprietario = proprietario   # OBJETO, que virá da classe PESSOA - DADOS DA PESSOA

    print("\nDADOS do VEICULO:")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Cor: {carro.cor}")
    print(f"Placa: {carro.placa}")
    print(f"Ano: {carro.ano}")
    print(f"DADOS DO PROPRIETARIO:\n{carro.infor_proprietario()}")


if __name__ == "__main__":
    main()