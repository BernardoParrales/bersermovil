# Pruebas de los modelos y servicios
from bersermovil.servicios.iservice import IService

# Funcion para testear los metodos de los servicios
def test(op=None, servicio=None, obj=None):
    valor = None
    if op == 1:
        # Create
        valor = servicio.create(obj)
    elif op == 2:
        # Read
        valor = servicio.read(obj)
    elif op == 3:
        # Read_all
        valor = servicio.read_all()
    elif op == 4:
        # Update
        valor = servicio.update(obj)
    elif op == 5:
        # Delete
        valor = servicio.delete(obj)
    
    print(valor)
    return valor

# NUMERO_TELENOFO
# Import
from bersermovil.servicios.numeroservice import NumeroService
from bersermovil.modelos.numero import NumeroTelofono
    
def prueba_numero():
    # Prueba del objeto
    estados = ["activo", "inactivo"]
    numero = NumeroTelofono(None, None, 0, "0999585829", estados[1])
    print(numero.to_string())
    # Prueba del servicio
    numero_service = NumeroService()
    test(2, numero_service, numero)
prueba_numero()

# BANCOS
from bersermovil.servicios.bancoservices import BancoService
from bersermovil.modelos.banco import Banco

def prueba_banco():
    banco = Banco(3, "Banco del Austro")
    print(banco.to_string())
    
    banco_service = BancoService()
    test(5, banco_service, banco)
    
#prueba_banco()
from bersermovil.servicios.personaservice import PersonaService
from bersermovil.modelos.persona import Persona

def prueba_persona():
    persona = Persona(None, "Juan", "Garcia", "0999999998")
    print(persona.to_string())
    
    persona_servicio = PersonaService()
    test(5, persona_servicio, persona)
    
#prueba_persona()

from bersermovil.servicios.paqueteservice import PaqueteService
from bersermovil.modelos.paquete import Paquete

def prueba_paquete():
    paquete = Paquete(4, 4, "Paquete de 4$ con 4096 MB", 4096, 5)
    print(paquete.to_string())
    
    paquete_service = PaqueteService()
    test(5, paquete_service, paquete)
    
#prueba_paquete()
from bersermovil.servicios.cuentabancariaservice import CuentaBancariaService
from bersermovil.modelos.cuentabancaria import CuentaBancaria

def prueba_cuentabancaria():
    cuentabancaria = CuentaBancaria(3, 1, 2, 5)
    print(cuentabancaria.to_string())
    
    cuentabancaria_service = CuentaBancariaService()
    test(5, cuentabancaria_service, cuentabancaria)
    
#prueba_cuentabancaria()

from bersermovil.servicios.saldoservice import SaldoService
from bersermovil.modelos.saldo import Saldo

def prueba_saldo():
    saldo = Saldo(4, 9, 0)
    print(saldo.to_string())
    
    saldo_servicio = SaldoService()
    test(5, saldo_servicio, saldo)
    
#prueba_saldo()



