class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        print("Produto: ", self.nome)
        print("Preço: ", self.preco)
        print("Quantidade: ", self.quantidade) #Quando tiver fora de aspas não precisa de "f" nem chave

    def calcular_total_estoque(self):
        total = self.preco * self.quantidade
        print(f"Valor total em estoque: {total:.2f}") #aspas

p1 = Produto("Mouse", 50.00, 10)
p2 = Produto("Teclado", 120.00, 5)

p1.mostrar_dados()
p1.calcular_total_estoque()

p2.mostrar_dados()
p2.calcular_total_estoque()

