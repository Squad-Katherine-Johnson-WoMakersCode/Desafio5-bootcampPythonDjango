produto
    nome
    categoria
    quantidade
    fornecedor (classe)(lista de fornecedor)
        método diminuir estoque


class Produto:
    def __init__(self, nome, categoria, quantidade, fornecedor):
        self.nome = ""
        self.categoria = ""
        self.quantidade = 0
        self.fornecedor = []

    def get_nome(self):
        return self.nome
    
    def get_categoria(self):
        return self.categoria

    def get_quantidade(self):
        return self.quantidade

    def get_fornecedor(self):
        return self.fornecedor

    def diminuir_estoque(self):
    
    