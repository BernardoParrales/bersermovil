# Agregar todos los imports de los modelos
from bersermovil.servicios.saldoservice import SaldoService
from bersermovil.servicios.paqueteservice import PaqueteService
from bersermovil.servicios.numeroservice import NumeroService
from bersermovil.servicios.personaservice import PersonaService
from bersermovil.servicios.bancoservices import BancoService
from bersermovil.servicios.cuentabancariaservice import CuentaBancariaService

from bersermovil.modelos.persona import Persona
from bersermovil.modelos.numero import NumeroTelofono
from bersermovil.modelos.saldo import Saldo
from bersermovil.modelos.cuentabancaria import CuentaBancaria

class ControladorService:
    
    # Obtiene los paquetes disponibles para activar
    __paquete_service = PaqueteService()
    __bancos_service = BancoService()
    
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
    
    # OBJETO CUENTA BANCARIA
    # 0:id, 1:persona_id, 2:banco_id, 3:saldo
    __obj_cuenta_bancaria = CuentaBancaria()
    __cuenta_bancaria_service = CuentaBancariaService()


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
    
    def comprar_paquete_con_cuenta_bancaria(self, numero_cuenta, paquete):
        # Datos Paquete
        costo = paquete[1]
        megas = paquete[3]
        # Datos Fondo Actual Cuenta Bancaria
        obj_cuenta = CuentaBancaria(numero_cuenta)
        obj_fondo_actual = self.__cuenta_bancaria_service.read(obj_cuenta)
        fondo_actual = obj_fondo_actual[3]
        
        # Validar fondos para la compra
        if fondo_actual >= costo:    
            # Datos Saldo Actual Megas
            obj_saldo_actual = self.__saldo_service.read(self.__obj_saldo)
            saldo_actual_dolares = obj_saldo_actual[1]
            saldo_actual_megas = obj_saldo_actual[2]
            # Operaciones
            nuevo_fondo_actual = fondo_actual - costo
            nuevo_saldo_megas = saldo_actual_megas + megas
            
            # Actualizar registros
            obj_saldo = Saldo(obj_saldo_actual[0], saldo_actual_dolares, nuevo_saldo_megas)
            self.__saldo_service.update(obj_saldo)
            
            obj_cuenta = CuentaBancaria(numero_cuenta, obj_fondo_actual[1], obj_fondo_actual[2], nuevo_fondo_actual)
            self.__cuenta_bancaria_service.update(obj_cuenta)
            result = "Compra realiza con exito."
        else: result = "No se pudo realizar la compra."
        return result
    
    def compra_de_saldo_con_cuenta_bancaria(self, numero_cuenta, costo):
        # Datos Fondo Actual Cuenta Bancaria
        obj_cuenta = CuentaBancaria(numero_cuenta)
        obj_fondo_actual = self.__cuenta_bancaria_service.read(obj_cuenta)
        fondo_actual = obj_fondo_actual[3]
        
        # Validar fondos para la compra
        if fondo_actual >= costo:    
            # Datos Saldo Actual Megas
            obj_saldo_actual = self.__saldo_service.read(self.__obj_saldo)
            saldo_actual_dolares = obj_saldo_actual[1]
            saldo_actual_megas = obj_saldo_actual[2]
            # Operaciones
            nuevo_fondo_actual = fondo_actual - costo
            nuevo_saldo_dolares = saldo_actual_dolares + costo
            
            # Actualizar registros
            obj_saldo = Saldo(obj_saldo_actual[0], nuevo_saldo_dolares, saldo_actual_megas)
            self.__saldo_service.update(obj_saldo)
            
            obj_cuenta = CuentaBancaria(numero_cuenta, obj_fondo_actual[1], obj_fondo_actual[2], nuevo_fondo_actual)
            self.__cuenta_bancaria_service.update(obj_cuenta)
            result = "Compra realiza con exito."
        else: result = "No se pudo realizar la compra."
        return result
    
    def consultar_saldos(self):
        saldos = self.__saldo_service.read(self.__obj_saldo)
        return saldos
    
    def consultar_mi_numero(self):
        mi_numero = self.__obj_numero_telefono.get_numero_telefono()
        return mi_numero
    
    def consultar_mi_informacion(self):
        return self.__obj_persona
    
    def consultar_bancos(self):
        bancos = self.__bancos_service.read_all()
        return bancos
    
    def consultar_cedula(self, cedula):
        # Averiguar el id de la cuenta bancaria de la persona
        # 1. Buscar la cedula de la persona
        obj = Persona(None, None, None, cedula)
        consulta = self.__persona_service.buscar_por_cedula(obj)
        return consulta