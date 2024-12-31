class Loja:
    def __init__(self, nome: str, id_loja: int):
        self.nome = nome
        self.id_loja = id_loja

    def __str__(self):
        return f"Loja: {self.nome} (ID: {self.id_loja})"

