from api.ml.product import Produto
from api.ml.store import Loja

if __name__ == "__main__":
    loja_exemplo = Loja(nome="Loja Central", id_loja=101)
    produto_exemplo = Produto(
        nome="Smartphone XYZ",
        descricao="Um smartphone moderno com tela OLED de 6.5 polegadas.",
        id_produto=12345,
        preco=2499.99,
        quantidade=50,
        avaliacao=4.7,
        loja=loja_exemplo,
        imagens=["img1.jpg", "img2.jpg", "img3.jpg"],
        imagem_capa="img1.jpg"
    )
    
    print(produto_exemplo)