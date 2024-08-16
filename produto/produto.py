class Produto:
    def __init__(self, nome, categoria, quantidade, fornecedor):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.fornecedor = fornecedor #lista de fornecedores

    def get_nome(self):
        return self.nome
    
    def get_categoria(self):
        return self.categoria

    def get_quantidade(self):
        return self.quantidade

    def get_fornecedor(self):
        return self.fornecedor

    def diminuir_estoque(self, diminuir):
        self.quantidade = self.quantidade - diminuir

    def __str__(self):
        return f'Produto: {self.nome}\Categoria do produto: {self.categoria}\nEstoque: {self.quantidade}\nFornecedores: {self.fornecedor}'
    