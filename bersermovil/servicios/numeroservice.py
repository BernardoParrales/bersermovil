import bersermovil.servicios.conexion as conexion
from bersermovil.servicios.iservice import IService
from bersermovil.modelos.numero import NumeroTelofono
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
# NOTA: Cuando retorna un mayor o igual a 1 si se realizo el registro, ejemplo: if registro[0] >= 1
# NOTA: Solo se usa la variable "registro" cuando es una insersión

# Nombre de la Tabla: numeros_telefonos
# Campos de la base de datos: id_numero, persona_id, saldo_id, numero_telefono, estado[activo/inactivo] 
# (5 campos)
class NumeroService(IService):
        
    def create(self, obj=NumeroTelofono()):
        try:
            sql = "INSERT INTO numeros_telefonos VALUES(null, %s, %s, %s, %s)"
            registro = (obj.persona_id, 
                        obj.saldo_id,
                        obj.numero_telefono,
                        obj.estado)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]    
        return [cursor.rowcount, self]
    
    def read(self, obj=NumeroTelofono()):
        try:
            sql = f"SELECT * FROM numeros_telefonos WHERE numero_telefono = {obj.numero_telefono}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM numeros_telefonos"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=NumeroTelofono()):
        try:
            sql = f"UPDATE numeros_telefonos SET persona_id = %s, saldo_id = %s, estado = %s WHERE numero_telefono = {obj.numero_telefono}"
            registro = (obj.persona_id, obj.saldo_id, obj.estado)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=NumeroTelofono()):
        try:
            sql = f"DELETE FROM numeros_telefonos WHERE numero_telefono = {obj.numero_telefono}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
