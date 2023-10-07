class Passageiro:

    preço_viagem = {'Nova Iorque' : 10000, 'Nova Jersey' : 12000, 'Pittsburgh' : 8500}

    def __init__(self, nome, idade, destino):
        self.__nome = nome
        self.__idade = idade
        self.__destino = destino
        self.__milhas = self.__ac_milhas

    @staticmethod
    def viagens():
        return ('Nova Iorque', 'Nova Jersey', 'Pittsburgh')
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def destino(self):
        return self.__destino

    @property
    def milhas(self):
        return self.__milhas
    
    def __ac_milhas(self):
        self.__milhas += (self.preço_viagem[self.__destino] * 0.05)

        
        