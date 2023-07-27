import src.database as db
from flask import request, jsonify



database_path = ""

def init_db(database):
    global database_path
    database_path = database

def add_user():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"

        cursor = con.cursor()
        data = request.get_json()

        # Since the 'id' key might not exist in the data dictionary,
        # it's better to use the get() method with a default value.
        id = data.get("id_clientes")
        nombre = data.get("nombre")
        email = data.get("email")
        telefono = data.get("telefono")
        mensaje = data.get("mensaje")

        cursor.execute('INSERT INTO clientes (id_clientes ,nombre ,email , telefono ,mensaje) VALUES (%s, %s, %s, %s, %s)', (id ,nombre ,email , telefono ,mensaje))
        con.commit()
        con.close()

        print('Usuario agregado exitosamente')  # Add this line to check the function flow

        return "Usuario creado exitosamente"
    except Exception as e:
        print('Error:', str(e))  # Print the error message to diagnose the issue
        return "Error al agregar el usuario"

    
def get_user(id):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id_clientes = %s', (id,))
    data_user = cursor.fetchone()
    
    if data_user:
        data = {'id_clientes': data_user[0], 'nombre': data_user[1], 'email': data_user[2], 'telefono': data_user[3],'mensaje': data_user[4]}
        con.close()
        print(data)
        return jsonify(data)
    else:
        return 'The user was not found' 


def users_get():
    try:
        con = db.conectdb()
        if con is None:
            return "Error: No se pudo establecer la conexión a la base de datos"

        cursor = con.cursor()
        cursor.execute('SELECT * FROM clientes')
        users = cursor.fetchall()
        con.close()

        # Transform the data into the desired format
        formatted_users = []
        for user in users:
            formatted_user = {
                "id_clientes": user[0],
                "nombre": user[1],
                "email": user[2],
                "telefono": user[3],
                "mensaje": "cita gratuita"
            }
            formatted_users.append(formatted_user)

        return formatted_users
    except Exception as e:
        print("Error:", e)
        return "Error al obtener los usuarios"



def user_delete(id_delete):
    con = db.conectdb()
    cursor = con.cursor()
    cursor.execute('DELETE FROM clientes WHERE id_clientes = %s', (id_delete,))
    con.commit()
    con.close()
    return 'Product deleted'

def user_edit_clientes(id, data):
    con = db.conectdb()  # Assuming you have a function named connectdb() to establish a database connection
    cursor = con.cursor()

    if "nombre" in data:
        nombre = data["nombre"]
        cursor.execute('UPDATE clientes SET nombre = %s WHERE id_clientes = %s', (nombre, id))

    if "email" in data:
        email = data["email"]
        cursor.execute('UPDATE clientes SET email = %s WHERE id_clientes = %s', (email, id))

    if "telefono" in data:
        telefono = data["telefono"]
        cursor.execute('UPDATE clientes SET telefono = %s WHERE id_clientes = %s', (telefono, id))

    if "mensaje" in data:
        mensaje = data["mensaje"]
        cursor.execute('UPDATE clientes SET mensaje = %s WHERE id_clientes = %s', (mensaje, id))

    con.commit()
    con.close()

    return 'Data modified'  # Corrected spelling of "Data"

# Additional Notes:
# 1. Make sure to import the necessary modules (e.g., `import db`) for the code to work correctly.
# 2. Ensure that the `id_edit` exists in the database to perform the updates correctly.
