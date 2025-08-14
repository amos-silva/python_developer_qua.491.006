from dataclasses import dataclass
import Pessoa

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razao_social: str
    fantasia: str
    cnpj: str

    def __str__(self):
        return f"DADOS DA EMPRESA:\nRazão Social: {self.razao_social}\nNome Fantasia: {self.fantasia}\nCNPJ: {self.cnpj}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    