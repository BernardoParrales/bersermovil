import bersermovil.servicios.conexion as conexion
from bersermovil.servicios.iservice import IService
from bersermovil.modelos.cuentabancaria import CuentaBancaria
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
# NOTA: Cuando retorna un mayor o igual a 1 si se realizo el registro, ejemplo: if registro[0] >= 1
# NOTA: Solo se usa la variable "registro" cuando es una insersión

# Nombre de la Tabla: numeros_telefonos
# Campos de la base de datos: id_numero, persona_id, saldo_id, numero_telefono, estado[activo/inactivo] 
# (5 campos)
class CuentaBancariaService(IService):
        
    def create(self, obj=CuentaBancaria()):
        try:
            sql = "INSERT INTO cuentas_bancarias VALUES(null, %s, %s, %s)"
            registro = (obj.persona_id, 
                        obj.banco_id,
                        obj.saldo)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]    
        return [cursor.rowcount, self]
    
    def read(self, obj=CuentaBancaria()):
        try:
            sql = f"SELECT * FROM cuentas_bancarias WHERE id = {obj.id}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM cuentas_bancarias"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=CuentaBancaria()):
        try:
            sql = f"UPDATE cuentas_bancarias SET persona_id = %s, banco_id = %s, saldo = %s WHERE id = {obj.id}"
            registro = (obj.persona_id, obj.banco_id, obj.saldo)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=CuentaBancaria()):
        try:
            sql = f"DELETE FROM cuentas_bancarias WHERE id = {obj.id}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
