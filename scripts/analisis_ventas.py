import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga de datps
df = pd.read_csv('datos/ventas_simuladas.csv')

# 2. Convertir la columna de fecha a formato especializado de Pandas
df['sales_date'] = pd.to_datetime(df['sales_date'])

# 3. Cálculos principales
total_ventas = df['sales_amount'].sum()
print(f"--- REPORTE DE VENTAS ---")
print(f"Monto Total Recaudado: ${total_ventas:,.2f}")

# 4. Agrupación por mes (Resample)
# 'M' significa agrupar por el final de cada mes
ventas_mensuales = df.resample('M', on='sales_date')['sales_amount'].sum()
print("\nDesglose Mensual:")
print(ventas_mensuales)

# 5. Generación del Gráfico
plt.figure(figsize=(10, 6))
ventas_mensuales.plot(kind='line', marker='o', color='#2ca02c', linewidth=2)
plt.title('Evolución de Ventas - Ciclo 2024', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ventas ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Guardar el resultado en la carpeta correspondiente
plt.savefig('resultados/reporte_ventas.png')
print("\n[OK] Gráfico guardado en resultados/reporte_ventas.png")
