from db.conexion import get_connection

def insertar_cliente(nombre, apellido, dni, direccion, telefono, email):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO clientes (nombre, apellido, dni, direccion, telefono, email)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (nombre, apellido, dni, direccion, telefono, email))
        conn.commit()
        print("✅ Cliente insertado correctamente.")
    except Exception as e:
        print("❌ Error al insertar cliente:", e)
    finally:
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    insertar_cliente(
        "Juan", "Pérez", "45678901", "Av. Siempre Viva 742", "2617894561", "juan@mail.com"
    )
