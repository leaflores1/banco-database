from db.conexion import get_connection

def hacer_transferencia(cuenta_origen_id, cuenta_destino_id, monto):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # 1. Verificamos el saldo disponible en la cuenta origen
        cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_origen_id,))
        resultado = cursor.fetchone()
        if not resultado:
            print("❌ Cuenta origen no encontrada.")
            return
        saldo_origen = resultado[0]

        if saldo_origen < monto:
            print("❌ Saldo insuficiente.")
            return

        # 2. Restar saldo de cuenta origen
        cursor.execute("UPDATE cuentas SET saldo = saldo - %s WHERE id = %s", (monto, cuenta_origen_id))

        # 3. Sumar saldo a cuenta destino
        cursor.execute("UPDATE cuentas SET saldo = saldo + %s WHERE id = %s", (monto, cuenta_destino_id))

        # 4. Registrar la transacción
        cursor.execute("""
            INSERT INTO transacciones (tipo, monto, cuenta_origen_id, cuenta_destino_id)
            VALUES ('Transferencia', %s, %s, %s)
        """, (monto, cuenta_origen_id, cuenta_destino_id))

        conn.commit()
        print("✅ Transferencia realizada con éxito.")
    except Exception as e:
        print("❌ Error al hacer la transferencia:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    hacer_transferencia(cuenta_origen_id=1, cuenta_destino_id=2, monto=300.00)
