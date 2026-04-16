class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bibi!")

    def parar(self):
        print("Parando...")

    def correr(self):
        print("Correndo!")

    def registro(self):
        print("==========REGISTO BIKE==========")
        print(f"")

