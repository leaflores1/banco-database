from db.conexion import get_connection

def hacer_deposito():
    conn = get_connection()
    cursor = conn.cursor()

    cuenta_id = input("ID de la cuenta a depositar: ")
    monto = float(input("Monto a depositar: "))

    # Actualizar saldo
    cursor.execute("UPDATE cuentas SET saldo = saldo + %s WHERE id = %s", (monto, cuenta_id))

    # Registrar transacción
    cursor.execute("""
        INSERT INTO transacciones (tipo, monto, cuenta_destino_id)
        VALUES ('Depósito', %s, %s)
    """, (monto, cuenta_id))

    conn.commit()
    conn.close()

    print(f"✅ Depósito de ${monto:.2f} realizado con éxito en la cuenta {cuenta_id}")

if __name__ == "__main__":
    hacer_deposito()
