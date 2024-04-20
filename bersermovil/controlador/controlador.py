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
    def realizar_compra_de_paquete_con_saldo_en_dolares(self, paquete):
        result = self.__controlador_service.comprar_paquete(paquete)
        return result
    
    def realizar_compra_con_saldo_en_dolares(self):
        
        return 1
        
    def consultar_bancos_disponibles(self):
        return ["Banco Pinchincha", "Banco de Guayaquil", "Banco Bolivariano", "Banco del Pacifico"]  
    
    def validar_cedula(self, cedula): # Hace una consulta a la db para saber si existe dicha cedula
        return True
    
    def validar_cuenta_bancaria(self, numero_cuenta): # Hace una consulta a la db para saber si existe dicho numero
        return True
    
    # paquete, saldo en dolares
    def realizar_compra_cuenta_bancaria(self, valor, tipo_de_saldo=[]):
        valor_cuenta_actual = 20
        
        if valor <= valor_cuenta_actual:
            valor_Actual = valor_cuenta_actual - valor
            
            # Restar el valor a la cuenta bancaria
            # Sumar el saldo comprado
            
            return True
        else:
            return False
            
    def activar_tarjeta_prepago(self, numero_tarjeta):
        # Realizar una consulta para ver si existe el numero
        # Si existe se extrae el valor del saldo y se lo agrega al NUMERO de la cuenta asociada, return True
        # Caso contrario retorna False
        return True
    
    # Consultar Saldo es un metodo que retorna un array con el saldo actual de un numero
    def consultar_saldos(self):
        # Consulta los saldos actuales del numero
        result = self.__controlador_service.consultar_saldos()
        return result
    
    def consultar_mi_numero(self):
        mi_numero = self.__controlador_service.consultar_mi_numero()
        return mi_numero
    
    def consultar_mi_informacion(self):
        # Consultar informacion persona del nuemro asociado
        return [1, "Victor", "Parrales", "0944170288"]
        
        
        
        
        
        