import ContaCorrente as cc
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():

    conta = cc.ContaCorrente(nome="", cpf="", email="", profissao="", telefone="", endereco="", salario=0.0, agencia="", num_conta="", saldo=0.0)

    


    while True:
            try:
                print(" ---------- 🐍 BANCO COBRA 🐍 ----------")
                print("1 - Inserir dados do Cliente.")
                print("2 - Consultar dados da conta.")
                print("3 - Depositar.")
                print("4 - Sacar.")
                print("5 - SAIR.")                    
                opcao = input("Escolha uma opção: ").strip()
                limpar()

                match opcao:
                    case "1":

                        print("INSIRA OS DADOS DO USUARIO:\n")

                        cc.nome = input("Informe o NOME: ").strip().title()
                        cc.cpf = input("Informe o CPF: ").strip()
                        cc.email = input("EMAIL: ").strip()
                        cc.profissao = input("Profissão: ").strip().title()
                        cc.telefone = input("Telefone: ").strip().title()
                        cc.endereco = input("Endereço: ").strip().title()
                        cc.salario = float(input("Salário: ").replace(",",".")) 
                        cc.agencia = input("Agencia: ").strip().title()
                        cc.num_conta = input("Conta: ").strip().title()
                        cc.saldo = float(input("Saldo: ").replace(",","."))                      

                        continue

                    case "2":
                        cc.exibir_dados()
                        continue
            
                    case "3":
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
                        
                    case "4":
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

                    case "5":
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