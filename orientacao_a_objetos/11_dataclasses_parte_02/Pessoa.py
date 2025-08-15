from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Pessoa(ABC):  # ABC = abstrato, para evitar que Pesosa seja instanciada
    email: str
    telefone: str
    endereco: str

    @abstractmethod     # metodo simplismente para tornar a Classe Pessoa Abstrata - para não poder ser instanciada
    def __setattr__(self):
        pass