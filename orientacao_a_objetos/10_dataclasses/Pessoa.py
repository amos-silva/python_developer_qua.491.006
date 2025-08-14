from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    cpf: str
    idade: int
    altura: float
        
    def __str__(self):
        return f"\nDADOS DO USUARIO:\nNome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\nIdade: {len(self)}\nAltura: {self.altura}"

    def __len__(self):
        return self.idade