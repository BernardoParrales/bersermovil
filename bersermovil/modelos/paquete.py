class Paquete:
    def __init__(self, id, costo, descripcion, saldo_megas, dias):
        self.id = id
        self.costo = costo
        self.descripcion = descripcion
        self.saldo_megas = saldo_megas
        self.dias = dias
        
    def getId(self):
        return self.id
    
    def getCosto(self):
        return self.costo
    
    def getDescripcion(self):
        return self.descripcion
    
    def getSaldoMegas(self):
        return self.saldo_megas
    
    def getDias(self):
        return self.dias
    
    
        