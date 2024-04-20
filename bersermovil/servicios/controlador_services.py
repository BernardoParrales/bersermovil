# Agregar todos los imports de los modelos
from bersermovil.servicios.saldoservice import SaldoService
from bersermovil.servicios.paqueteservice import PaqueteService
from bersermovil.servicios.numeroservice import NumeroService
from bersermovil.servicios.personaservice import PersonaService

from bersermovil.modelos.persona import Persona
from bersermovil.modelos.numero import NumeroTelofono
from bersermovil.modelos.saldo import Saldo


class ControladorService:
    
    # Obtiene los paquetes disponibles para activar
    __paquete_service = PaqueteService()
    
    # OBJETO NUMERO TELEFONICO
    # 0:id_numero, 1:persona_id, 2:saldo_id, 3:numero_telefono, 4:estado
    __obj_numero_telefono = NumeroTelofono()
    __numero_service = NumeroService()
    
    # OBJETO SALDO
    # 0:id_saldo, 1:saldo_dolares, 2:saldo_megas
    __obj_saldo = Saldo()
    __saldo_service = SaldoService()
    
    # OBJETO PERSONA
    # 0:id_persona, 1:nombre, 2:apellido, 3:cedula
    __obj_persona = Persona()
    __persona_service = PersonaService()


    def __init__(self, numero_telefono=None):
        self.numero_telefono = numero_telefono
        self.obtener_objeto_numero_telefono(numero_telefono)
    
    def obtener_objeto_numero_telefono(self, numero_telefono):
        # Obtener objeto
        obj = NumeroTelofono(None, None, None, numero_telefono, None)
        result = self.__numero_service.read(obj)
        # Rellenar objeto numero_telefono
        self.__obj_numero_telefono.set_id(result[0])
        self.__obj_numero_telefono.set_persona_id(result[1])
        self.__obj_numero_telefono.set_saldo_id(result[2])
        self.__obj_numero_telefono.set_numero_telefono(numero_telefono)
        self.__obj_numero_telefono.set_estado(result[4])
        # Obtener los objetos faltantes
        self.obtener_objeto_saldo(self.__obj_numero_telefono.get_saldo_id())
        self.obtener_objeto_persona(self.__obj_numero_telefono.get_persona_id())
        
    def obtener_objeto_saldo(self, id_saldo):
        # Obtener el objeto actual
        obj = Saldo(id_saldo, None, None)
        result = self.__saldo_service.read(obj)
        # Rellenar objeto saldo
        self.__obj_saldo.set_id(id_saldo)
        self.__obj_saldo.set_saldo_dolares(result[1])
        self.__obj_saldo.set_saldo_megas(result[2])
        
    def obtener_objeto_persona(self, id_persona):
        # Obtener el objeto actual
        obj = Persona(id_persona, None, None, None)
        result = self.__persona_service.read(obj)
        # Rellenar el objeto persona
        self.__obj_persona.set_id(id_persona)
        self.__obj_persona.set_nombre(result[1])
        self.__obj_persona.set_apellido(result[2])
        self.__obj_persona.set_cedula(result[3])
        
    def mostrar_paquetes_disponibles(self):
        paquetes = self.__paquete_service.read_all()
        return paquetes
    
    def consultar_saldo_en_dolares_disponible(self):
        # Consultar el saldo con el id_saldo
        obj_saldo = self.__saldo_service.read(self.__obj_saldo)
        saldo_actual = obj_saldo[1]
        return saldo_actual
    
    # El paquete es de tipo Tupla (id_paquete, costo, descripcion, saldo_megas, dias)
    # SALDO = 0:id_saldo, 1:saldo_dolares, 2:saldo_megas
    def comprar_paquete(self, paquete):
        # Datos Paquete
        costo = paquete[1]
        megas = paquete[3]
        # Datos Saldo actual 
        obj_saldo_actual = self.__saldo_service.read(self.__obj_saldo)
        saldo_actual_dolares = obj_saldo_actual[1]
        saldo_actual_megas = obj_saldo_actual[2]
        # Operaciones
        nuevo_saldo_dolares = saldo_actual_dolares - costo
        nuevo_saldo_megas = saldo_actual_megas + megas
        # Actualizar registro
        obj = Saldo(obj_saldo_actual[0], nuevo_saldo_dolares, nuevo_saldo_megas)
        result = self.__saldo_service.update(obj)
        return result
    
    def consultar_saldos(self):
        saldos = self.__saldo_service.read(self.__obj_saldo)
        return saldos
    
    def consultar_mi_numero(self):
        mi_numero = self.__obj_numero_telefono.get_numero_telefono()
        return mi_numero