import bersermovil.servicios.conexion as conexion
from bersermovil.servicios.iservice import IService
from bersermovil.modelos.paquete import Paquete
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
# NOTA: Cuando retorna un mayor o igual a 1 si se realizo el registro, ejemplo: if registro[0] >= 1
# NOTA: Solo se usa la variable "registro" cuando es una insersión

# Nombre de la Tabla: numeros_telefonos
# Campos de la base de datos: id_numero, persona_id, saldo_id, numero_telefono, estado[activo/inactivo] 
# (5 campos)
class PaqueteService(IService):
        
    def create(self, obj=Paquete()):
        try:
            sql = "INSERT INTO paquetes VALUES(null, %s, %s, %s, %s)"
            registro = (obj.costo, 
                        obj.descripcion,
                        obj.saldo_megas,
                        obj.dias)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]    
        return [cursor.rowcount, self]
    
    def read(self, obj=Paquete()):
        try:
            sql = f"SELECT * FROM paquetes WHERE id_paquete = {obj.id}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM paquetes"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=Paquete()):
        try:
            sql = f"UPDATE paquetes SET costo = %s, descripcion = %s, saldo_megas = %s, dias = %s WHERE id_paquete = {obj.id}"
            registro = (obj.costo, obj.descripcion, obj.saldo_megas, obj.dias)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=Paquete()):
        try:
            sql = f"DELETE FROM paquetes WHERE id_paquete = {obj.id}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
