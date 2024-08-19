from cliente.cliente import Cliente
from transacao.transacao import Transacao
class Mercado:
    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = []  
        self.__transacoes = []  

    @property
    def nome(self):
        return self.__nome

    @property
    def clientes(self):
        return self.__clientes

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("O objeto deve ser uma instância da classe Cliente")
        if cliente in self.__clientes:
            raise ValueError("Cliente já está registrado no mercado")
        self.__clientes.append(cliente)
    
    def realizar_transacao(self, cliente, produto, quantidade):
        if cliente not in self.__clientes:
            raise ValueError("Cliente não registrado no mercado")
        
        transacao = Transacao(cliente, produto, quantidade)
        self.__transacoes.append(transacao)
        return transacao  

    def listar_clientes(self):
        return self.__clientes
    
    def listar_transacoes(self):
        return self.__transacoes