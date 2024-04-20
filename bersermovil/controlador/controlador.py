from bersermovil.servicios.controlador_services import ControladorService

class Controlador:
    
    # Constructor
    def __init__(self, numero_telefono):
        self.numero_telefono = numero_telefono
        self.__controlador_service = ControladorService(numero_telefono)
    
    def consultar_paquetes_disponible(self):
        paquetes = self.__controlador_service.mostrar_paquetes_disponibles()
        return paquetes
    
    # Consulta el saldo actual en dolares para validar...
    def consultar_saldo_en_dolares(self):
        saldo_actual = self.__controlador_service.consultar_saldo_en_dolares_disponible()
        return saldo_actual
    
    # El paquete es de tipo Tupla (id_paquete, costo, descripcion, saldo_megas, dias)
    def realizar_compra_de_paquete_con_saldo_en_dolares(self,numero_cuenta, paquete):
        result = self.__controlador_service.comprar_paquete_con_cuenta_bancaria(numero_cuenta, paquete)
        return result
    
    def realizar_compra_de_saldo_con_cargo_cuenta_bancaria(self, numero_cuenta, paquete):
        result = self.__controlador_service.compra_de_saldo_con_cuenta_bancaria(numero_cuenta, paquete)
        return result
        
    def consultar_bancos_disponibles(self):
        bancos = self.__controlador_service.consultar_bancos()
        return bancos
    
    # Hace una consulta a la db para saber si existe dicha cedula
    def validar_cedula(self, cedula):
        result = self.__controlador_service.consultar_cedula(cedula)
        return result
    
    # Consultar Saldo es un metodo que retorna un array con el saldo actual de un numero
    def consultar_saldos(self):
        # Consulta los saldos actuales del numero
        result = self.__controlador_service.consultar_saldos()
        return result
    
    def consultar_mi_numero(self):
        mi_numero = self.__controlador_service.consultar_mi_numero()
        return mi_numero
    
    # Consultar informacion persona del nuemro asociado
    def consultar_mi_informacion(self):
        info = self.__controlador_service.consultar_mi_informacion()
        return info
        
        
        
        
        
        