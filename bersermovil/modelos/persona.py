class Persona:
    
    def __init__(self, id=None, nombre=None, apellido=None, cedula=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_cedula(self):
        return self.cedula
    
    def set_id(self, id):
        self.id = id
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def set_cedula(self, cedula):
        self.cedula = cedula
        
    def to_string(self):
        return f"{self.id}, {self.nombre}, {self.apellido}, {self.cedula}"