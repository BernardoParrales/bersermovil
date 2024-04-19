from bersermovil.modelos.saldo import Saldo
from bersermovil.servicios.iservice import IService
from bersermovil.servicios.conexion import conectar

connect = conectar()
database = connect[0]
cursor = connect[1]

class SaldoService(IService):
        
    def create(self, obj=Saldo()):
        try:
            sql = "INSERT INTO saldos VALUES(null, %s, %s)"
            registro = (obj.saldo_dolares,
                        obj.saldo_megas)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]    
        return [cursor.rowcount, self]
    
    # Requiere el ID
    def read(self, obj=Saldo()):
        try:
            sql = f"SELECT * FROM saldos WHERE id_saldo = {obj.id}"
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self] 
        return result
    
    def read_all(self):
        try:
            sql = "SELECT * FROM saldos"
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return result
    
    def update(self, obj=Saldo()):
        try:
            sql = f"UPDATE saldos SET saldo_dolares = %s, saldo_megas = %s WHERE id_saldo = {obj.id}"
            registro = (obj.saldo_dolares, obj.saldo_megas)
            cursor.execute(sql, registro)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self]
    
    def delete(self, obj=Saldo()):
        try:
            sql = f"DELETE FROM saldos WHERE id_saldo = {obj.id}"
            cursor.execute(sql)
            database.commit()
        except Exception as e:
            return [cursor.rowcount, type(e).__name__, self]
        return [cursor.rowcount, self] 
