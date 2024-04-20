# ¡IMPORTANTE! Los servicios piden un Objeto de su tipo, NO datos como str o int
from bersermovil.servicios.controlador_services import ControladorService

control_service = ControladorService("0999585829")

def prueba_mpd():
    paquetes = control_service.mostrar_paquetes_disponibles()
    print(paquetes)
#prueba_mpd()

from bersermovil.modelos.numero import NumeroTelofono

def prueba_csedd():
    saldo = control_service.consultar_saldo_en_dolares_disponible()
    print(saldo)
#prueba_csedd()

def prueba_ec():
    cedula = control_service.consultar_cedula("094417028")
    print(cedula)
    
prueba_ec()