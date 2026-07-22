class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro acelerou para {self.velocidade} km/h.")
    
    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            print(f"O carro reduziu sua velocidade para {self.velocidade} km/h.")

        
    def mostrar_dados(self):
        print("A marca do carro é: ", self.marca)
        print("O modelo do carro é: ", self.modelo)
        print("O ano do carro é: ", self.ano)
        print("A velocidade do carro é: ", self.velocidade)

car1 = Carro("Fiat", "Fiat 500", 2017)

car1.acelerar()
car1.acelerar()
car1.acelerar()
car1.frear()
print()

car1.mostrar_dados()