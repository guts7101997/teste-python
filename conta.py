class Conta:

    limites = {'BB': 1000.0, 'Bradesco': 800.0, 'Caixa': 1200.0}

    def __init__(self, titular, numero, banco, agencia, saldo):
        self._titular = titular
        self._numero = numero
        self._banco = banco
        self._agencia = agencia
        self._saldo = saldo
        self._limite = self.limites[banco]
        self._milhas = 0
        

    @property
    def titular(self):
        return self._titular

    @property
    def numero(self):
        return self._numero

    @property
    def banco(self):
        return self._banco

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def limite(self):
        return self._limite
    
    def extrato(self):
        return (f'Saldo de {self._saldo} do titular {self._titular}')
    
    def _pode_sacar(self, valor):
        if (self._saldo + self._limite >= valor):
            return True
        
    def saque(self, valor):
        if (self._pode_sacar(valor)):
            self._saldo -= valor
            self._milhas += (valor * 0.05)

    def depósito(self, valor):
        self._limite += valor

    @property
    def milhas(self):
        return self.__milhas


    