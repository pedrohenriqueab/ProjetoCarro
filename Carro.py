class Carro(object):
    def __init__(self, cor, model, ano):
        self.cor = cor
        self.model = model
        self.ano = ano

    def acelerar(self):
        pass

    def freiar(self):
        pass

    def __str__(self):
        return "[Cor: %s, Model: %s, Ano: %i]" % (self.cor, self.model, self.ano)


