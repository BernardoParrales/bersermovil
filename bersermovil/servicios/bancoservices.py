import bersermovil.servicios.conexion as conexion
from bersermovil.servicios.iservice import IService
from bersermovil.modelos.banco import Banco

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# NOTA: Cuando retorna un mayor o igual a 1 si se realizo el registro, ejemplo: if registro[0] >= 1

# Nombre de la Tabla: bancos
# Campos de la base de datos: id_numero, persona_id, saldo_id, numero_telefono, estado[activo/inactivo] 
# (5 campos)
class BancoService(IService):
        
    def create(self, obj=Banco()):
        try:
            sql = "INSERT INTO bancos VALUES(null, %s)"
            registro = [obj.nombre]
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, e,self]    
        return [cursor.rowcount, self]
    
    def read(self, obj=Banco()):
        try:
            sql = f"SELECT * FROM bancos WHERE nombre = {obj.nombre}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM bancos"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=Banco()):
        try:
            sql = f"UPDATE bancos SET nombre = %s WHERE id_banco = {obj.id}"
            registro = (obj.nombre)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=Banco()):
        try:
            sql = f"DELETE FROM bancos WHERE id_banco = {obj.id}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
