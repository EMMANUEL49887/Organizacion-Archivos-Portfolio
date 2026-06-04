import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("ventas_tecnologia.csv")

# Mostrar datos del archivo
print("\n=== DATOS DEL ARCHIVO ===")
print(df)

# Crear columna ingresos
df["ingresos"] = df["cantidad"] * df["precio_unitario"]

# ==================================
# REPORTES TABULARES
# ==================================

# Ventas por producto
ventas_producto = df.groupby("producto")["cantidad"].sum()

print("\n=== VENTAS POR PRODUCTO ===")
print(ventas_producto)

# Ingresos por mes
ventas_mes = df.groupby("mes")["ingresos"].sum()

print("\n=== INGRESOS POR MES ===")
print(ventas_mes)

# Ingresos por producto
ingresos_producto = df.groupby("producto")["ingresos"].sum()

print("\n=== INGRESOS POR PRODUCTO ===")
print(ingresos_producto)

# Producto más vendido
producto_mas_vendido = ventas_producto.idxmax()

print("\n=== PRODUCTO MÁS VENDIDO ===")
print(producto_mas_vendido)

# ==================================
# GRÁFICA DE BARRAS
# ==================================

plt.figure(figsize=(8,5))

ventas_producto.plot(kind='bar')

plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

plt.show()

# ==================================
# GRÁFICA DE LÍNEAS
# ==================================

plt.figure(figsize=(8,5))

ventas_mes.plot(kind='line', marker='o')

plt.title("Ingresos por Mes")
plt.xlabel("Mes")
plt.ylabel("Ingresos")

plt.grid(True)

plt.show()

# ==================================
# GRÁFICA CIRCULAR
# ==================================

plt.figure(figsize=(7,7))

ventas_producto.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Porcentaje de Ventas por Producto")

plt.ylabel("")

plt.show()

# ==================================
# ANÁLISIS FINAL
# ==================================

producto_mayor_ingreso = ingresos_producto.idxmax()
producto_menos_vendido = ventas_producto.idxmin()
mes_mas_rentable = ventas_mes.idxmax()

print("\n=== ANÁLISIS FINAL ===")

print("Producto con mayores ingresos:", producto_mayor_ingreso)
print("Producto menos vendido:", producto_menos_vendido)
print("Mes más rentable:", mes_mas_rentable)