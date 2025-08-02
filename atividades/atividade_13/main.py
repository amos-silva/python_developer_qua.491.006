"""
# criar um aplicativo de banco , com seguintes dados:
Titular da conta
CPF
Agencia
N. da conta
Saldo

# o usuario pode fazer:
Consultar dados
Depositar valor
Sacar valor
imprimir extrato (gerar arquivo)
sair do programa
"""
import classes as cl


# ALGORITIMO PRINCIPAL
if __name__ == "__main__":
    conta = cl.Conta(
        titular="",
        cpf="",
        agencia="",
        num_conta="",
        saldo=""
    )


# INPUT
while True:
        try:
            print("1 - Cadastrar novo Correntista.")
            print("2 - Consultar dados da conta.")
            print("3 - Depositar.")
            print("4 - Sacar.")
            print("5 - Extrato.")
            print("6 - SAIR.")                    
            opcao = input("Escolha uma opção: ").strip()

            ...

            match opcao:
                case "1":
                    r = float(input("Informe o Raio: ").replace(",", "."))
                    print(f"A Area do circulo é: {mo.area(r)}")
                
                case "2":
                    r = float(input("Informe o Raio: ").replace(",", "."))
                    print(f"A Circunferencia do circulo é: {mo.circ(r)}")

                case "3":
                    print("SAIU ! ")
                    break
                
                case _:
                    print("Opção invalida")
                    continue        
        except Exception as e:
            print("ERRO, {e}")
            continue





"""
try:
    conta.titular = input("Informe seu Nome: ").strip().title()
    conta.cpf = input("Informe seu CPF: ").strip().title()
    conta.agencia = input("Informe a Agencia: ").strip().title()
    conta.num_conta = input("Informe N. da Conta: ").strip().title()
    conta.saldo = float(input("Saldo: ").replace(",", "."))

# CHAMAR O METODO
    print(conta.apresentar())

except Exception as e:
    print("ERRO ao criar Objeto. {e}")
"""