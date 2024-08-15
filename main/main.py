from cliente.cliente import Cliente
from fornecedor.fornecedor import Fornecedor
from mercado.mercado import Mercado
from produto.produto import Produto
from transacao.transacao import Transacao

def instanciar_clientes():
    cliente1 = Cliente()
    cliente2 = Cliente()
    cliente3 = Cliente()
    
    return cliente1, cliente2, cliente3

def instanciar_produtos():
    produto1 = Produto()
    produto2 = Produto()
    produto3 = Produto()
    
    return produto1, produto2, produto3

def instanciar_fornecedores():
    fornecedor1 = Fornecedor()
    fornecedor2 = Fornecedor()
    fornecedor3 = Fornecedor() 

    return fornecedor1, fornecedor2, fornecedor3

def instanciar_mercado():
    cliente1, cliente2, cliente3 = instanciar_clientes()
    produto1, produto2, produto3 = instanciar_produtos()

    transacao1 = Transacao(cliente1, produto1, 2)
    transacao2 = Transacao(cliente2, produto2, 3)
    transacao3 = Transacao(cliente3, produto3, 1)
    
    mercado = Mercado("Mercearia da Esquina")
    
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
    print(mercado.listar_clientes())
    print("\nTRANSAÇÕES:\n")
    print(mercado.listar_transacoes())

main()