class Persona:
    
    def __init__(self, id, nombre, apellido, cedula):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getCedula(self):
        return self.cedula
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido
        
    def setCedula(self, cedula):
        self.cedula = cedula
        
    def toString(self):
        return f"{self.id}, {self.nombre}, {self.apellido}, {self.cedula}"