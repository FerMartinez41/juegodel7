import random
class Dado:
    def __init__(self):
        self.dado = 0

    def tirarDado(self):
        self.valor = random.randint(1, 6)

    def getValor(self):
        return self.valor
