from api.ml.store import Loja

class Produto:
    def __init__(
        self, 
        nome: str, 
        descricao: str, 
        id_produto: int, 
        preco: float, 
        quantidade: int, 
        avaliacao: float, 
        loja: Loja, 
        imagens: list[str], 
        imagem_capa: str
    ):
        self.nome = nome
        self.descricao = descricao
        self.id_produto = id_produto
        self.preco = preco
        self.quantidade = quantidade
        self.avaliacao = avaliacao
        self.loja = loja
        self.imagens = imagens
        self.imagem_capa = imagem_capa

    def __str__(self):
        return (
            f"Produto: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"ID: {self.id_produto}\n"
            f"Preço: R${self.preco:.2f}\n"
            f"Quantidade em Estoque: {self.quantidade}\n"
            f"Avaliação: {self.avaliacao}/5.0\n"
            f"{self.loja}\n"
            f"Imagem de Capa: {self.imagem_capa}\n"
            f"Imagens: {', '.join(self.imagens)}"
        )
