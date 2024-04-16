class NumeroTelofono:
    def __init__(self, id=None, persona_id=None, saldo_id=None, numero_telefono=None, estado=None):
        self.id = id
        self.persona_id = persona_id
        self.saldo_id = saldo_id
        self.numero_telefono = numero_telefono
        self.estado = estado
        
    def get_id(self):
        return self.id
    
    def get_persona_id(self):
        return self.persona_id
    
    def get_saldo_id(self):
        return self.saldo_id
    
    def get_numero_telefono(self):
        return self.numero_telefono
    
    def get_estado(self):
        return self.estado
    
    def to_string(self):
        return f"{self.id}, {self.persona_id}, {self.saldo_id}, {self.numero_telefono}, {self.estado}"
    
    def set_persona_id(self, persona_id):
        self.persona_id = persona_id
        
    def set_saldo_id(self, saldo_id):
        self.saldo_id = saldo_id
        
    def set_numero_telefono(self, numero_telefono):
        self.numero_telefono = numero_telefono
        
    def set_estado(self, estado):
        self.estado = estado