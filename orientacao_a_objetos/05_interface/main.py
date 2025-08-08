import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    cc = c.ContaCorrente(titular="", cpf="", agencia="", num_conta="", saldo=0.0)

    #SETAR OS VALORES
    print("INSIRA OS DADOS DO USUARIO:\n")

    cc.titular = input("Informe o NOME: ").strip().title()
    cc.cpf = input("Informe o CPF: ").strip()
    cc.agencia = input("Agencia: ").strip().title()
    cc.num_conta = input("Numero da Conta: ").strip().title()


    while True:
            try:
                print(" ---------- 🐍 BANCO COBRA 🐍 ----------")
                print("1 - Consultar dados da conta.")
                print("2 - Depositar.")
                print("3 - Sacar.")
                print("4 - SAIR.")                    
                opcao = input("Escolha uma opção: ").strip()
                limpar()

                match opcao:
                    case "1":
                        cc.consultar_dados()
                        continue
            
                    case "2":
                        try:
                            valor = float(input("Informe o valor do DEPOSITO: R$ ").replace(",","."))
                            if valor > 0:
                                print(f"Deposito efetuado com Sucesso. Novo Saldo R$ {cc.depositar(valor):.2f}")                                
                            else:
                                print("Valor invalido")
                                
                        except Exception as e:
                            print(f"ERRO. {e}")
                        finally:
                            continue                    
                        
                    case "3":
                        try:
                            valor = float(input("Informe o valor do SAQUE: R$ ").replace(",","."))
                            if valor > 0:
                                if valor <= cc.saldo:
                                    print(f"SAQUE efetuado com Sucesso. Novo Saldo R$ {cc.sacar(valor):.2f}")   
                                else:
                                    print("Saldo INSUFICIENTE!")
                            else:
                                print("Valor invalido")
                                
                        except Exception as e:
                            print(f"ERRO. {e}")
                        finally:
                            continue  

                    case "4":
                        print("VC SAIU DA CONTA! ")
                        break
                    
                    case _:
                        print("Opção invalida")
                        continue        
            except Exception as e:
                print("ERRO, {e}")
                continue



if __name__ == "__main__":
    main()
