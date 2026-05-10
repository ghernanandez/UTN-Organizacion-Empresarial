import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos/ventas_simuladas.csv')
df.columns = df.columns.str.strip()
df.rename(columns={'sales date': 'sales_date'}, inplace=True) 

df['sales_date'] = pd.to_datetime(df['sales_date'])

total_ventas = df['sales amount'].sum()
producto_top = df.groupby('product_id')['sales amount'].sum().idxmax()
ventas_mensuales = df.resample('M', on='sales_date')['sales amount'].sum()

print(f"Total Ventas: ${total_ventas:,.2f}")
print(f"Producto ID mas vendido: {producto_top}")
print(ventas_mensuales)

plt.figure(figsize=(10, 6))
ventas_mensuales.plot(kind='line', marker='o', color='blue')
plt.title('Reporte Mensual de Ventas')
plt.grid(True)
plt.savefig('resultados/reporte_ventas.png')
