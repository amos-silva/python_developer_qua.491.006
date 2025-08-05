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
import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# ALGORITIMO PRINCIPAL
if __name__ == "__main__":

    # Instancia da Classe Conta
    conta = c.Conta(titular="", cpf="", agencia="", num_conta="", saldo=0.0)

    # Define os valores dos atributos da Classe
    print(" ---------- 🐍 BANCO COBRA 🐍 ----------")
    conta.titular = input("Informe o nome do Titular: ").strip().title()
    conta.cpf = input("Informe o CPF: ").strip()
    conta.agencia = "1010-1"
    conta.num_conta = "102030-1"
    limpar()

    while True:
            try:
                print(" ---------- 🐍 BANCO COBRA 🐍 ----------")
                print("1 - Consultar dados da conta.")
                print("2 - Depositar.")
                print("3 - Sacar.")
                print("4 - Extrato.")
                print("5 - SAIR.")                    
                opcao = input("Escolha uma opção: ").strip()
                limpar()

                match opcao:
                    case "1":
                        conta.consultar_dados()
                        continue
            
                    case "2":
                        try:
                            valor = float(input("Informe o valor do DEPOSITO: R$ ").replace(",","."))
                            if valor > 0:
                                print(f"Deposito efetuado com Sucesso. Novo Saldo R$ {conta.depositar(valor):.2f}")                                
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
                                if valor <= conta.saldo:
                                    print(f"SAQUE efetuado com Sucesso. Novo Saldo R$ {conta.sacar(valor):.2f}")   
                                else:
                                    print("Saldo INSUFICIENTE!")
                            else:
                                print("Valor invalido")
                                
                        except Exception as e:
                            print(f"ERRO. {e}")
                        finally:
                            continue  
                    case "4":
                        try:
                            conta.extrato()
                            print("Extrato impresso com sucesso!")
                            
                                
                        except Exception as e:
                            print(f"ERRO ao IMPRIMIR. {e}")
                        finally:
                            continue

                    case "5":
                        print("VC SAIU DA CONTA! ")
                        break
                    
                    case _:
                        print("Opção invalida")
                        continue        
            except Exception as e:
                print("ERRO, {e}")
                continue
