# Pruebas de los modelos y servicios

# NUMERO_TELENOFO
# Import
from bersermovil.servicios.numeroservice import NumeroService
from bersermovil.modelos.numero import NumeroTelofono
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
    
# Prueba del objeto
estados = ["activo", "inactivo"]
numero = NumeroTelofono(None, None, 0, "0999999995", estados[1])
print(numero.to_string())

# Prueba del servicio
numero_service = NumeroService()

test(5, numero_service, numero)