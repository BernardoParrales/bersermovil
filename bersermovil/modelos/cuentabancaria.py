class CuentaBancaria:
    def __init__(self, id, persona_id, banco_id, saldo):
        self.id = id
        self.persona_id = persona_id
        self.banco_id = banco_id
        self.saldo = saldo
        
    def getId(self):
        return self.id
    
    def getPersona_id(self):
        return self.persona_id
    
    def getBanco_id(self):
        return self.banco_id
    
    def getSaldo(self):
        return self.saldo
    
    def toString(self):
        return f"{self.id}, {self.persona_id}, {self.banco_id}, {self.saldo}"
    
    def setSaldo(self, saldo):
        self.saldo = saldo
        