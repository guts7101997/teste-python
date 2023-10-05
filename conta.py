class Conta:

    limites = {'BB': 1000.0, 'Bradesco': 800.0, 'Caixa': 1200.0}

    def __init__(self, titular, numero, banco, agencia, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__banco = banco
        self.__agencia = agencia
        self.__saldo = saldo
        self.__limite = self.limites[banco]
        self.__milhas = 0
        

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def banco(self):
        return self.__banco

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def limite(self):
        return self.__limite
    
    def extrato(self):
        return (f'Saldo de {self.__saldo} do titular {self.__titular}')
    
    def pode_sacar(self, valor):
        if (self.__saldo + self.__limite >= valor):
            return True
        
    def saque(self, valor):
        if (self.pode_sacar(valor)):
            self.__saldo -= valor
            self.__milhas += (valor * 0.05)

    def depósito(self, valor):
        self.__limite += valor

    @property
    def milhas(self):
        return self.__milhas


    