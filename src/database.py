#1. We need is a connector: mysql-conector
import mysql.connector

def conectdb():
    host = "127.0.0.1"
    user = "root"
    passwd = "CONTRASEÑA"
    database = "clientes_sebastian"
    port = 3306
    
    try:
        con = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database,
            port=port,
        )
        print("Conexión exitosa a la base de datos")
        return con
    except mysql.connector.Error as error:
        print(f"Error al conectarse a la base de datos: {error}")
        return None