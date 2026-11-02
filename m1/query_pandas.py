
import pandas as pd
import psutil
import os
import time

archivo = "data/yellow_tripdata_2025-01.parquet"

# Proceso actual de Python
proceso = psutil.Process(os.getpid())

def memoria_mb():
    return proceso.memory_info().rss / (1024 ** 2)

# Memoria inicial
memoria_inicial = memoria_mb()

# 1. Cargar Parquet
inicio = time.perf_counter()

df = pd.read_parquet(archivo)

tiempo_carga = time.perf_counter() - inicio
memoria_carga = memoria_mb()

print(f"Filas: {len(df):,}")
print(f"Tiempo de carga: {tiempo_carga:.4f} segundos")
print(f"Memoria adicional tras carga: {memoria_carga - memoria_inicial:.2f} MB")
print(f"Tamaño del DataFrame: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# 2. GROUP BY
inicio = time.perf_counter()

resultado = (
    df.groupby("PULocationID")
    .agg(
        viajes=("PULocationID", "size"),
        promedio=("total_amount", "mean")
    )
    .sort_values("viajes", ascending=False)
    .head(10)
)

tiempo_groupby = time.perf_counter() - inicio

print("\nTop 10 zonas:")
print(resultado)

print(f"\nTiempo GROUP BY: {tiempo_groupby:.4f} segundos")
print(f"Memoria del proceso al finalizar: {memoria_mb():.2f} MB")
print(f"Tiempo total carga + GROUP BY: {tiempo_carga + tiempo_groupby:.4f} segundos")
