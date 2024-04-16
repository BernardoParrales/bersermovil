class Paquete:
    def __init__(self, id, costo, descripcion, saldo_megas, dias):
        self.id = id
        self.costo = costo
        self.descripcion = descripcion
        self.saldo_megas = saldo_megas
        self.dias = dias
        
    def get_id(self):
        return self.id
    
    def get_costo(self):
        return self.costo
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_saldo_megas(self):
        return self.saldo_megas
    
    def get_dias(self):
        return self.dias
    
    
        