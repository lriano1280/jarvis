
import duckdb
import time

# 1. Conectarse a DuckDB
con = duckdb.connect()

# Ruta del archivo Parquet
archivo = "data/yellow_tripdata_2025-01.parquet"

# 2. Contar las filas
inicio = time.perf_counter()

total = con.execute(f"""
    SELECT COUNT(*)
    FROM '{archivo}'
""").fetchone()[0]

tiempo_count = time.perf_counter() - inicio

print(f"Total de filas: {total:,}")
print(f"Tiempo COUNT: {tiempo_count:.4f} segundos")

# 3. Ejecutar GROUP BY
inicio = time.perf_counter()

resultado = con.execute(f"""
    SELECT
        PULocationID,
        COUNT(*) AS viajes,
        AVG(total_amount) AS promedio
    FROM '{archivo}'
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
""").fetchall()

tiempo_groupby = time.perf_counter() - inicio

print("\nTop 10 zonas:")
for zona, viajes, promedio in resultado:
    print(f"Zona {zona}: {viajes:,} viajes, promedio ${promedio:.2f}")

print(f"\nTiempo GROUP BY: {tiempo_groupby:.4f} segundos")

con.close()
