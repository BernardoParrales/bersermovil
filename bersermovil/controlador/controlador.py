class Controlador:
    
    # Constructor
    def __init__(self, numero_telefono):
        self.numero_telefono = numero_telefono
    
    # Consulta el saldo actual en dolares para validar...
    def consultar_saldo_en_dolares(self):
        return 1
    
    def realizar_compra_con_saldo_en_dolares(self, valor):
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
        return [5, 250]
    
    def consultar_mi_numero(self):
        # Consultar mi numero
        return "0999585829"
    
    def consultar_mi_informacion(self):
        # Consultar informacion persona del nuemro asociado
        return [1, "Victor", "Parrales", "0944170288"]
        
        
        
        
        
        