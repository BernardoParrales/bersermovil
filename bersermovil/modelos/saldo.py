class Saldo:
    def __init__(self, id=None, saldo_dolares=None, saldo_megas=None):
        self.id = id
        self.saldo_dolares = saldo_dolares
        self.saldo_megas = saldo_megas
        
    def to_string(self):
        return f"{self.id}, {self.saldo_dolares}, {self.saldo_megas}"
        