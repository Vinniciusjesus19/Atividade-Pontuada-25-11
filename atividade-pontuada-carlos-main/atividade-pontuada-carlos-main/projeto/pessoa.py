from projeto.models.endereco import Endereco
from abc import ABC,abstractmethod
class Pessoa(ABC):
    def __init__(self,id:int, nome:str, telefone:str, email:str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.telefone =telefone
        self.email = email
        self.endereco = endereco
    @abstractmethod
    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")