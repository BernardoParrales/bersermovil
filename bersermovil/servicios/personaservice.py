import bersermovil.servicios.conexion as conexion
from bersermovil.servicios.iservice import IService
from bersermovil.modelos.persona import Persona
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
# NOTA: Cuando retorna un mayor o igual a 1 si se realizo el registro, ejemplo: if registro[0] >= 1
# NOTA: Solo se usa la variable "registro" cuando es una insersión

# Nombre de la Tabla: numeros_telefonos
# Campos de la base de datos: id_numero, persona_id, saldo_id, numero_telefono, estado[activo/inactivo] 
# (5 campos)
class PersonaService(IService):
    
    def create(self, obj=Persona()):
        try:
            sql = "INSERT INTO personas VALUES(null, %s, %s, %s)"
            registro = (obj.nombre,
                        obj.apellido,
                        obj.cedula)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]    
        return [cursor.rowcount, self]
    
    def read(self, obj=Persona()):
        try:
            sql = f"SELECT * FROM personas WHERE id_persona = {obj.id}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM personas"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=Persona()):
        try:
            sql = f"UPDATE personas SET nombre = %s, apellido = %s WHERE cedula = {obj.cedula}"
            registro = (obj.nombre, obj.apellido)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=Persona()):
        try:
            sql = f"DELETE FROM personas WHERE cedula = {obj.cedula}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
