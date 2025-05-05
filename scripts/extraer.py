from db.conexion import get_connection

def hacer_extraccion():
    conn = get_connection()
    cursor = conn.cursor()

    cuenta_id = input("ID de la cuenta a extraer: ")
    monto = float(input("Monto a extraer: "))

    # Verificar saldo disponible
    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    resultado = cursor.fetchone()

    if not resultado:
        print("❌ Cuenta no encontrada.")
        return

    saldo_actual = resultado[0]
    if saldo_actual < monto:
        print("❌ Saldo insuficiente.")
        return

    # Actualizar saldo
    cursor.execute("UPDATE cuentas SET saldo = saldo - %s WHERE id = %s", (monto, cuenta_id))

    # Registrar transacción
    cursor.execute("""
        INSERT INTO transacciones (tipo, monto, cuenta_origen_id)
        VALUES ('Extracción', %s, %s)
    """, (monto, cuenta_id))

    conn.commit()
    conn.close()

    print(f"✅ Extracción de ${monto:.2f} realizada con éxito desde la cuenta {cuenta_id}")

if __name__ == "__main__":
    hacer_extraccion()
