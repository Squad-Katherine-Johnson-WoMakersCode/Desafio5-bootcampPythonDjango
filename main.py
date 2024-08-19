from cliente.cliente import Cliente
from fornecedor.fornecedor import Fornecedor
from produto.produto import Produto
from mercado.mercado import Mercado

fornecedor1 = Fornecedor(nome="Fornecedor A")
fornecedor2 = Fornecedor(nome="Fornecedor B")
fornecedor3 = Fornecedor(nome="Fornecedor C")

def instanciar_clientes():
    cliente1 = Cliente(nome="Pedro Gonçalves", telefone="9999-9999", endereco="Rua A, 123")
    cliente2 = Cliente(nome="Luiza Oliveira", telefone="8888-8888", endereco="Rua B, 456")
    cliente3 = Cliente(nome="Carolina Souza", telefone="7777-7777", endereco="Rua C, 789")
    
    return cliente1, cliente2, cliente3


def instanciar_produtos():
    produto1 = Produto(nome="Arroz", categoria="Alimentos", quantidade=50, fornecedor = fornecedor1) 
    produto2 = Produto(nome="Feijão", categoria="Alimentos", quantidade=30, fornecedor = fornecedor2)
    produto3 = Produto(nome="Macarrão", categoria="Alimentos", quantidade=100, fornecedor = fornecedor3)
    
    return produto1, produto2, produto3


def instanciar_mercado():
    cliente1, cliente2, cliente3 = instanciar_clientes()
    produto1, produto2, produto3 = instanciar_produtos()

    mercado = Mercado(nome="Mercearia da Esquina")
    
    mercado.adicionar_cliente(cliente1)
    mercado.adicionar_cliente(cliente2)
    mercado.adicionar_cliente(cliente3)
    
    mercado.realizar_transacao(cliente=cliente1, produto=produto1, quantidade=2)
    mercado.realizar_transacao(cliente=cliente2, produto=produto2, quantidade=3)
    mercado.realizar_transacao(cliente=cliente3, produto=produto3, quantidade=1)
    
    return mercado

def main():
    mercado = instanciar_mercado()
    print("\nCLIENTES:\n")
    for cliente in mercado.listar_clientes():
        print(cliente)
        
    print("\nTRANSAÇÕES:\n")
    for transacao in mercado.listar_transacoes():
        print(transacao)

main()