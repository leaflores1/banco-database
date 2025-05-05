import random
from db.conexion import get_connection

def generar_numero_cuenta():
    return f"0001-{random.randint(100000, 999999)}"

def crear_cuenta():
    conn = get_connection()
    cursor = conn.cursor()

    print("👉 Iniciando creación de cuenta")

    dni = input("DNI del cliente: ")

    # Verificar si el cliente existe
    cursor.execute("SELECT id, nombre, apellido FROM clientes WHERE dni = %s", (dni,))
    cliente = cursor.fetchone()

    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    cliente_id, nombre, apellido = cliente
    print(f"Cliente encontrado: {nombre} {apellido}")

    tipo = input("Tipo de cuenta (Caja de ahorro / Cuenta corriente): ")
    if tipo not in ['Caja de ahorro', 'Cuenta corriente']:
        print("❌ Tipo inválido.")
        return

    numero_cuenta = generar_numero_cuenta()

    # Insertar cuenta en la base
    cursor.execute("""
        INSERT INTO cuentas (numero_cuenta, tipo, saldo, cliente_id)
        VALUES (%s, %s, %s, %s)
    """, (numero_cuenta, tipo, 0.00, cliente_id))

    conn.commit()
    conn.close()

    print(f"✅ Cuenta creada: {numero_cuenta} para {nombre} {apellido}")

if __name__ == "__main__":
    crear_cuenta()
