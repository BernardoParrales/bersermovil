class Saldo:
    def __init__(self, id=None, saldo_dolares=None, saldo_megas=None):
        self.id = id
        self.saldo_dolares = saldo_dolares
        self.saldo_megas = saldo_megas
        
    def get_id(self):
        return self.id
    
    def get_saldo_dolares(self):
        return self.saldo_dolares
    
    def get_saldo_megas(self):
        return self.saldo_megas
    
    def set_id(self, id):
        self.id = id
        
    def set_saldo_dolares(self, saldo_dolares):
        self.saldo_dolares = saldo_dolares
        
    def set_saldo_megas(self, saldo_megas):
        self.saldo_megas = saldo_megas
    
    def to_string(self):
        return f"{self.id}, {self.saldo_dolares}, {self.saldo_megas}"
        