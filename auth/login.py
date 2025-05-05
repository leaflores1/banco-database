from db.conexion import get_connection

def verificar_credenciales(dni, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM clientes WHERE dni = %s AND email = %s"
    cursor.execute(query, (dni, email))
    cliente = cursor.fetchone()
    conn.close()
    return cliente
