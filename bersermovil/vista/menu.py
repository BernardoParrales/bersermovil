# Menu 
from bersermovil.vista.componentes import indice, tr
from bersermovil.controlador.controlador import Controlador

OPINVALID = "Opción invalida"

class Menu:
       
    def __init__(self, numero_telefono):
        self.numero_telefono = numero_telefono
        self.__controlador = Controlador(numero_telefono)
        self.menu_principal()
        
        
    def menu_principal(self):
        tr()
        print("BERSERMOVIL\nMenú Principal")
        indice(["Paquetes", "Recargas", "Consulta de Saldos", "Otros Servicios", "Información Arcotel", "Salir"])
        opcion = input()
        tr()
        
        if opcion == "1":
            self.menu_paquetes()

        elif opcion == "2":
            self.menu_recargas()

        elif opcion == "3":
            self.menu_consulta_saldos()

        elif opcion == "4":
            self.menu_otros_servicios()

        elif opcion == "5":
            self.infomacion_arcotel()         
        
    def menu_paquetes(self):
        # Atributos de un paquete: 0:id_paquete, 1:costo, 2:descripcion, 3:saldo_megas, 4:dias
        paquetes = self.__controlador.consultar_paquetes_disponible()
        contador = 0
        for paquete in paquetes: 
            print(f"{paquete[0]}. {paquete[2]}.") 
            contador += 1
        id_paquete = int(input())
        tr()
        print(id_paquete)
        if id_paquete > 0 and id_paquete <= contador:
            self.menu_compra_paquete(paquetes[(id_paquete-1)])
        else:
            print("Fuera del rango")
               
    # Recibe una tupla del paquete seleccionado
    def menu_compra_paquete(self, paquete):
        print("Metodo de Compra para Activar el Paquete")
        indice(["Con Saldo en Dolares", "Cargo a Cuenta Bancaria", "Atras"])
        opcion = input()
        tr()
        
        if opcion == "1": self.menu_compra_paquete_con_saldo_en_dolares(paquete)
        if opcion == "2": self.menu_compra_paquete_con_cargo_cuenta_bancaria(paquete)
        
    # COMPRAR EL PAQUETE CON SALDO EN DOLARES   
    def menu_compra_paquete_con_saldo_en_dolares(self, paquete):
        print("Compra con Saldo en Dolares")
        saldo_en_dolares = self.__controlador.consultar_saldo_en_dolares() # Realizar compra de saldo en dolares
        
        if saldo_en_dolares >= paquete[1]: 
            self.__controlador.realizar_compra_de_paquete_con_saldo_en_dolares(paquete)
            print(f"Se a realizado la compra del {paquete[2]}")
        else:
            print(f"Saldo insuficiente. Tu saldo actual es de {saldo_en_dolares}$\n") 
            #exit()
            self.menu_saldo_insuficiente(paquete)
        
    # Atributos: id, saldo en dolares, saldo en megas        
    def menu_saldo_insuficiente(self, paquete):
        print(f"¿Desea comprar {paquete} con cuenta bancaria?")
        indice(["Si.", "Volver al menu principal.", "Salir."])
        opcion = input()
        tr()
        if opcion == "1": self.menu_compra_paquete_con_cargo_cuenta_bancaria(paquete)
        elif opcion == "2": self.menu_principal()
        else: exit()
            
    # paquete, saldo en dolares
    def menu_compra_paquete_con_cargo_cuenta_bancaria(self, paquete): # El tipo de saldo identifica el tipo de salgo (dolares o megas)
        print("Ingrese el número de cuenta")
        numero_cuenta = input()
        result = self.__controlador.realizar_compra_de_paquete_con_saldo_en_dolares(numero_cuenta, paquete)
        print(result)
        
    def menu_recargas(self):
        print("Recargas")
        indice(["Recargar saldo en dolares", "Atras", "Salir"])
        opcion = input()
        tr()
        if opcion == "1": self.menu_recargar_saldo_en_dolares()
        if opcion == "2": self.menu_principal()
        else: exit()

          
    def menu_recargar_saldo_en_dolares(self):
        print("Ingrese la cantidad de saldo en dolares a recargar en multiplos de 1.\nPor ejemplo: 1, 2, 3, 10...")
        try:
            cantidad_saldo_dolares = int(input())
            self.menu_compra_con_cargo_cuenta_bancaria(cantidad_saldo_dolares, ["saldo en dolares", cantidad_saldo_dolares])
            tr()
        except Exception:
            print("Valor invalido.")
            exit()
        
        
    def menu_consulta_saldos(self):
        print("Consulta de Saldos")
        saldos = self.__controlador.consultar_saldos()
        print(f"Tu saldo actual es:\nSaldo total en dolares: {saldos[1]}$\nSaldo de megas de paquetes: {saldos[2]} MB")
        indice(["Atras", "Salir"])
        opciones = input()
        if opciones == "1": self.menu_principal()
        tr()
        
    def menu_otros_servicios(self):
        print("Otros Servicios")
        indice(["Mi número", "Mi información", "Volver", "Salir"])
        opciones = input()
        tr()
        if opciones == "1": self.mostrar_mi_numero()
        elif opciones == "2": self.mostrar_mi_informacion()
        elif opciones == "3": self.menu_principal()
            
    def mostrar_mi_numero(self):
        mi_numero = self.__controlador.consultar_mi_numero()
        print(f"Mi número es: {mi_numero}")
        tr()
        
    # Persona: id, nombre, apellido, cedula
    def mostrar_mi_informacion(self):
        mi_informacion = self.__controlador.consultar_mi_informacion()
        print(f"Información del propietario del número teléfonico:\nNombre: {mi_informacion.get_nombre()}\nApellido: {mi_informacion.get_apellido()}\nNúmero de Cédula: {mi_informacion.get_cedula()}")
        tr()
        
    def infomacion_arcotel(self):
        print("Información Arcotel\nARCOTEL informa que tienes derecho a la entrega de tu factura física o electrónica...")
        
        



