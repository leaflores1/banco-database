from db.conexion import get_connection

def ver_transacciones_por_cuenta(cuenta_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        t.id, t.tipo, t.monto, t.fecha,
        co.numero_cuenta AS origen,
        cd.numero_cuenta AS destino
    FROM transacciones t
    LEFT JOIN cuentas co ON t.cuenta_origen_id = co.id
    LEFT JOIN cuentas cd ON t.cuenta_destino_id = cd.id
    WHERE t.cuenta_origen_id = %s OR t.cuenta_destino_id = %s
    ORDER BY t.fecha DESC
    """

    try:
        cursor.execute(query, (cuenta_id, cuenta_id))
        transacciones = cursor.fetchall()

        if not transacciones:
            print("No se encontraron transacciones para esta cuenta.")
            return

        print(f"\n📄 Transacciones para la cuenta ID {cuenta_id}:\n")
        for t in transacciones:
            print(f"{t['fecha']} - {t['tipo']} - ${t['monto']:.2f} | De: {t['origen']} → A: {t['destino']}")
    except Exception as e:
        print("❌ Error al obtener transacciones:", e)
    finally:
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    ver_transacciones_por_cuenta(1)
