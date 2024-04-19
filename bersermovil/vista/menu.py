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
        if opcion == "2": self.menu_compra_con_cargo_cuenta_bancaria(paquete)
        
    # COMPRAR EL PAQUETE CON SALDO EN DOLARES   
    def menu_compra_paquete_con_saldo_en_dolares(self, paquete):
        print("Compra con Saldo en Dolares")
        saldo_en_dolares = self.__controlador.consultar_saldo_en_dolares() # Realizar compra de saldo en dolares
        
        if saldo_en_dolares >= paquete[1]: 
            self.__controlador.realizar_compra_de_paquete_con_saldo_en_dolares(paquete)
            print(f"Se a realizado la compra del {paquete[2]}")
        else:
            print(f"Saldo insuficiente. Tu saldo actual es de {saldo_en_dolares}$\n") 
            exit()
            #self.menu_saldo_insuficiente(valor, ["paquete", valor])
        
    # Atributos: id, saldo en dolares, saldo en megas        
    def menu_saldo_insuficiente(self, valor, tipo_de_saldo=[]):
        print(f"Saldo insuficiente.\n¿Desea comprar {tipo_de_saldo[0]} con cuenta bancaria?")
        indice(["Si.", "Volver al menu principal.", "Salir."])
        opcion = input()
        tr()
        if opcion == "1": self.menu_compra_con_cargo_cuenta_bancaria(valor, tipo_de_saldo)
        elif opcion == "2": self.menu_principal()
        else: exit()
            
    # paquete, saldo en dolares
    def menu_compra_con_cargo_cuenta_bancaria(self, valor, tipo_de_saldo=[]): # El tipo de saldo identifica el tipo de salgo (dolares o megas)
        print("Elija el banco:")
        controla = control.Controlador(self.numero_telefono)
        bancos = controla.consultar_bancos_disponibles() # Consulta todos los bancos disponibles
        indice(bancos) # Selecciona el banco
        try:
            opcion = int(input()) # Comprueba que el valor ingresado sea el correcto
            if opcion >= 0: # Valida el rango de las opciones
                banco_seleccionado = bancos[opcion-1] # Guarda el banco seleccionado
                cedula = input("Ingrese el número de cédula: ") 
                validar_cedula = controla.validar_cedula(cedula) # Valida que la cedula sea real
                if validar_cedula: 
                    id_cuenta_bancaria = input("Ingrese número de cuenta: ")
                    valida_cuenta_bancaria = controla.validar_cuenta_bancaria(banco_seleccionado, id_cuenta_bancaria) # Valida la existencia de la cuenta del usuario
                    if valida_cuenta_bancaria:
                        comprobar_compra = controla.realizar_compra_cuenta_bancaria(valor, tipo_de_saldo) # Return True si se realizo la compra
                        if comprobar_compra:
                            print("Se realizo la compra con exito.")
                            self.menu_principal()
                        else:
                            print("Saldo insuficiente para realizar la compra.")
                    else:
                        print("Cuenta bancaria no existe.")
                else:
                    print("Cédula no existe.")
            else:
                print("Opción invalida.")                            
        except Exception:
            print("Opción invalida.")
            exit()
        
    def menu_recargas(self):
        print("Recargas")
        indice(["Activación de Tarjeta Prepago", "Recargar saldo en dolares", "Atras", "Salir"])
        opcion = input()
        tr()
        if opcion == "1": self.menu_activar_tarjeta_prepago()
        if opcion == "2": self.menu_recargar_saldo_en_dolares()
        if opcion == "3": self.menu_principal()
        else: exit()
        
    # Validar que la tarjeta exista en la BD
    def menu_activar_tarjeta_prepago(self):
        print("Ingrese el número de la tarjeta:")
        numero_tarjeta = input()
        controla = control.Controlador()
        activo_tarjeta = controla.activar_tarjeta_prepago(numero_tarjeta)
        
        if activo_tarjeta: print("Se activo la tarjeta con exito.")
        else: print("Número de la tarjeta invalido.")

          
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
        controla = control.Controlador(self.numero_telefono)
        mi_numero = controla.consultar_mi_numero()
        print(f"Mi número es: {mi_numero}")
        tr()
        
    def mostrar_mi_informacion(self):
        controla = control.Controlador(self.numero_telefono)
        mi_informacion = controla.consultar_mi_informacion()
        print(f"Información del propietario del número teléfonico:\nNombre: {mi_informacion[1]}\nApellido: {mi_informacion[2]}\nNúmero de Cédula: {mi_informacion[3]}")
        tr()
        
    def infomacion_arcotel(self):
        print("Información Arcotel\nARCOTEL informa que tienes derecho a la entrega de tu factura física o electrónica...")
        
        



