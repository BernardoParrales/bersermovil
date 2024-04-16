class Banco:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre
        
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def to_string(self):
        return f"{self.id}, {self.nombre}"
    