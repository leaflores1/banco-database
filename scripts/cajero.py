from auth.login import verificar_credenciales
from db.conexion import get_connection
import sys

def ver_cuentas(cliente_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, numero_cuenta, tipo, saldo FROM cuentas WHERE cliente_id = %s", (cliente_id,))
    cuentas = cursor.fetchall()
    conn.close()

    if not cuentas:
        print("⚠️ No tenés cuentas registradas.")
    else:
        print("\n💳 Tus cuentas:")
        for c in cuentas:
            print(f"  ID: {c['id']} | {c['tipo']} - {c['numero_cuenta']} → Saldo: ${c['saldo']:.2f}")
    return cuentas

def hacer_deposito(cliente_id):
    cuentas = ver_cuentas(cliente_id)
    cuenta_id = input("\nID de cuenta para depositar: ")
    monto = float(input("Monto a depositar: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE cuentas SET saldo = saldo + %s WHERE id = %s", (monto, cuenta_id))
    cursor.execute("""
        INSERT INTO transacciones (tipo, monto, cuenta_destino_id)
        VALUES ('Depósito', %s, %s)
    """, (monto, cuenta_id))
    conn.commit()
    conn.close()
    print("✅ Depósito realizado.")

def hacer_extraccion(cliente_id):
    cuentas = ver_cuentas(cliente_id)
    cuenta_id = input("\nID de cuenta para extraer: ")
    monto = float(input("Monto a extraer: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    saldo = cursor.fetchone()[0]

    if saldo < monto:
        print("❌ Saldo insuficiente.")
        return

    cursor.execute("UPDATE cuentas SET saldo = saldo - %s WHERE id = %s", (monto, cuenta_id))
    cursor.execute("""
        INSERT INTO transacciones (tipo, monto, cuenta_origen_id)
        VALUES ('Extracción', %s, %s)
    """, (monto, cuenta_id))
    conn.commit()
    conn.close()
    print("✅ Extracción realizada.")

def hacer_transferencia(cliente_id):
    cuentas = ver_cuentas(cliente_id)
    cuenta_origen = input("\nID de cuenta origen: ")
    cuenta_destino = input("ID de cuenta destino: ")
    monto = float(input("Monto a transferir: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_origen,))
    saldo = cursor.fetchone()[0]

    if saldo < monto:
        print("❌ Saldo insuficiente.")
        return

    cursor.execute("UPDATE cuentas SET saldo = saldo - %s WHERE id = %s", (monto, cuenta_origen))
    cursor.execute("UPDATE cuentas SET saldo = saldo + %s WHERE id = %s", (monto, cuenta_destino))
    cursor.execute("""
        INSERT INTO transacciones (tipo, monto, cuenta_origen_id, cuenta_destino_id)
        VALUES ('Transferencia', %s, %s, %s)
    """, (monto, cuenta_origen, cuenta_destino))
    conn.commit()
    conn.close()
    print("✅ Transferencia realizada.")

def menu_principal(cliente_id):
    while True:
        print("\n=== Menú del Cajero ===")
        print("1. Ver cuentas")
        print("2. Depositar")
        print("3. Extraer")
        print("4. Transferir")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            ver_cuentas(cliente_id)
        elif opcion == "2":
            hacer_deposito(cliente_id)
        elif opcion == "3":
            hacer_extraccion(cliente_id)
        elif opcion == "4":
            hacer_transferencia(cliente_id)
        elif opcion == "5":
            print("👋 Hasta luego.")
            sys.exit()
        else:
            print("❌ Opción inválida.")

def login():
    print("=== Inicio de sesión ===")
    dni = input("DNI: ")
    email = input("Email: ")
    cliente = verificar_credenciales(dni, email)

    if cliente:
        print(f"\n✅ Bienvenido, {cliente[1]} {cliente[2]}")
        menu_principal(cliente[0])
    else:
        print("❌ Credenciales incorrectas.")

if __name__ == "__main__":
    login()
