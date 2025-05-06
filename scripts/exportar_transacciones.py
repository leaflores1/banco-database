import pandas as pd
import os
from db.conexion import get_connection

def exportar_transacciones(cuenta_id=None):
    conn = get_connection()

    query = """
    SELECT 
        t.id, t.tipo, t.monto, t.fecha,
        co.numero_cuenta AS origen,
        cd.numero_cuenta AS destino
    FROM transacciones t
    LEFT JOIN cuentas co ON t.cuenta_origen_id = co.id
    LEFT JOIN cuentas cd ON t.cuenta_destino_id = cd.id
    """

    if cuenta_id:
        query += f" WHERE co.id = {cuenta_id} OR cd.id = {cuenta_id}"

    df = pd.read_sql(query, conn)
    conn.close()

    if df.empty:
        print("⚠️ No se encontraron transacciones.")
        return

    # Crear carpeta exports si no existe
    os.makedirs("exports", exist_ok=True)

    nombre_archivo = f"exports/transacciones_cuenta_{cuenta_id}.csv" if cuenta_id else "exports/transacciones_todas.csv"
    df.to_csv(nombre_archivo, index=False)

    print(f"✅ Transacciones exportadas a {nombre_archivo}")

if __name__ == "__main__":
    print("=== Exportar Transacciones ===")
    cuenta = input("ID de cuenta (Enter para todas): ").strip()
    exportar_transacciones(cuenta_id=int(cuenta) if cuenta else None)
