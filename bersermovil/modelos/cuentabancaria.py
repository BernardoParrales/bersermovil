class CuentaBancaria:
    def __init__(self, id, persona_id, banco_id, saldo):
        self.id = id
        self.persona_id = persona_id
        self.banco_id = banco_id
        self.saldo = saldo
        
    def get_id(self):
        return self.id
    
    def get_persona_id(self):
        return self.persona_id
    
    def get_banco_id(self):
        return self.banco_id
    
    def get_saldo(self):
        return self.saldo
    
    def to_string(self):
        return f"{self.id}, {self.persona_id}, {self.banco_id}, {self.saldo}"
    
    def set_saldo(self, saldo):
        self.saldo = saldo
        