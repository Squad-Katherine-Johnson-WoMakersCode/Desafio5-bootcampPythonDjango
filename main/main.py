from cliente.cliente import Cliente
from fornecedor.fornecedor import Fornecedor
from mercado.mercado import Mercado
from produto.produto import Produto
from transacao.transacao import Transacao

def instanciar_clientes():
    cliente1 = Cliente(nome="Pedro Gonçalves", telefone="9999-9999", endereco="Rua A, 123")
    cliente2 = Cliente(nome="Luiza Oliveira", telefone="8888-8888", endereco="Rua B, 456")
    cliente3 = Cliente(nome="Carolina Souza", telefone="7777-7777", endereco="Rua C, 789")
    
    return cliente1, cliente2, cliente3

def instanciar_produtos(fornecedores):
    produto1 = Produto(nome="Arroz", categoria="Alimentos", quantidade=50, fornecedores=fornecedores)
    produto2 = Produto(nome="Feijão", categoria="Alimentos", quantidade=30, fornecedores=fornecedores)
    produto3 = Produto(nome="Macarrão", categoria="Alimentos", quantidade=100, fornecedores=fornecedores)
    
    return produto1, produto2, produto3

def instanciar_fornecedores():
    fornecedor1 = Fornecedor(nome="Fornecedor A")
    fornecedor2 = Fornecedor(nome="Fornecedor B")
    fornecedor3 = Fornecedor(nome="Fornecedor C")

    return fornecedor1, fornecedor2, fornecedor3

def instanciar_mercado():
    cliente1, cliente2, cliente3 = instanciar_clientes()
    fornecedores = instanciar_fornecedores()
    produto1, produto2, produto3 = instanciar_produtos(fornecedores)

    transacao1 = Transacao(data="2024-08-19", cliente=cliente1, produto=produto1, quantidade=2)
    transacao2 = Transacao(data="2024-08-19", cliente=cliente2, produto=produto2, quantidade=3)
    transacao3 = Transacao(data="2024-08-19", cliente=cliente3, produto=produto3, quantidade=1)
    
    mercado = Mercado(nome="Mercearia da Esquina")
    
    mercado.adicionar_cliente(cliente1)
    mercado.adicionar_cliente(cliente2)
    mercado.adicionar_cliente(cliente3)
    
    mercado.adicionar_transacao(transacao1)
    mercado.adicionar_transacao(transacao2)
    mercado.adicionar_transacao(transacao3)
    
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