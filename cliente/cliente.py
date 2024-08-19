class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone

    def get_endereco(self):
        return self.endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}"
