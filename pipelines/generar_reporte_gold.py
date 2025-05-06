import pandas as pd
import os

def generar_reporte_gold():
    entrada = "exports/transacciones_limpias_3.csv"
    salida = "exports/reporte_gold_3.csv"

    if not os.path.exists(entrada):
        print(f"❌ Archivo no encontrado: {entrada}")
        return

    df = pd.read_csv(entrada)

    # Agrupar por cuenta y mes
    resumen = df.groupby(["origen", "año", "mes", "movimiento"]).agg(
        total_monto=pd.NamedAgg(column="monto", aggfunc="sum"),
        cantidad_op=pd.NamedAgg(column="id", aggfunc="count")
    ).reset_index()

    # Pivot para tener ingresos y egresos por fila
    tabla_pivot = resumen.pivot_table(
        index=["origen", "año", "mes"],
        columns="movimiento",
        values=["total_monto", "cantidad_op"],
        fill_value=0
    )

    # Flatten columnas
    tabla_pivot.columns = ['_'.join(col).lower() for col in tabla_pivot.columns]
    tabla_pivot.reset_index(inplace=True)

    # Calcular saldo neto
    tabla_pivot["saldo_neto"] = tabla_pivot.get("total_monto_ingreso", 0) - tabla_pivot.get("total_monto_egreso", 0)

    # Guardar reporte
    tabla_pivot.to_csv(salida, index=False)
    print(f"✅ Reporte Gold generado: {salida}")

if __name__ == "__main__":
    generar_reporte_gold()
