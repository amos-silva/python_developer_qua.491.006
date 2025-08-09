# classe interface de conta
from abc import ABC
from abc import abstractmethod

class IConta(ABC):
    # metodos de ação  -  que devo obrigar a conta usar esses metodos
    @abstractmethod
    def exibir_dados(self):
        pass
    @abstractmethod
    def depositar(self, valor):
        pass
    @abstractmethod
    def sacar(self, valor):
        pass