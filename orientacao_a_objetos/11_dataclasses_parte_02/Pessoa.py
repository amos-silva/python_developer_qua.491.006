from dataclasses import dataclass

@dataclass
class Pessoa:  # ABC = abstrato, para evitar que Pesosa seja instanciada
    email: str
    telefone: str
    endereco: str