import pandas as pd
import os

def procesar_transacciones():
    ruta_entrada = "exports/transacciones_cuenta_3.csv"
    ruta_salida = "exports/transacciones_limpias_3.csv"

    if not os.path.exists(ruta_entrada):
        print(f"❌ Archivo no encontrado: {ruta_entrada}")
        return

    print("📥 Leyendo archivo CSV...")
    df = pd.read_csv(ruta_entrada)

    # Limpiar valores nulos
    df.fillna("N/A", inplace=True)

    # Convertir fecha a datetime
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Agregar columnas derivadas
    df["año"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month

    # Clasificar como ingreso o egreso
    def clasificar_mov(row):
        if row["tipo"] in ["Depósito", "Transferencia"] and row["destino"] != "N/A":
            return "Ingreso"
        elif row["tipo"] in ["Extracción", "Transferencia"] and row["origen"] != "N/A":
            return "Egreso"
        return "Otro"

    df["movimiento"] = df.apply(clasificar_mov, axis=1)

    # Guardar resultado
    df.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo limpio generado: {ruta_salida}")

if __name__ == "__main__":
    procesar_transacciones()
