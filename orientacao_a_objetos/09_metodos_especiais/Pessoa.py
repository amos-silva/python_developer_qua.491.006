class Pessoa:
    def __init__(self, nome, idade):    # metodo Construtor
        self.nome = nome
        self.idade = idade

    def __str__(self):  # Retorna string dentro de uma frase
        return f"Olá, meu nome é {self.nome}, e tenho {self.idade} anos"
    
    def __len__(self):  # só funcionca com tipo INTEIRO
        return self.idade

    def __del__(self):
        print(f"Objeto {self.nome} destuido com sucesso")