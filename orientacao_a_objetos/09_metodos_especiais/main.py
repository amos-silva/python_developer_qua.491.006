import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Amós", idade=99)

    print(usuario)
    print(f"Idade: {len(usuario)}")

    # destruir o objeto - LIMPEZA DA MEMORIA
    del(usuario)
    

if __name__ == "__main__":
    main()