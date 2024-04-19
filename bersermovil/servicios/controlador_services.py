# Agregar todos los imports de los modelos
from bersermovil.servicios.saldoservice import SaldoService
from bersermovil.servicios.paqueteservice import PaqueteService
from bersermovil.modelos.persona import Persona

class ControladorService:
    
    __paquete_service = PaqueteService()
    
    def __init__(self, obj=Persona()):
        self.persona = obj
        
    def mostrar_paquetes_disponibles(self):
        paquetes = self.__paquete_service.read_all()
        return paquetes
    
    def comprar_paquete(self):
        
        return