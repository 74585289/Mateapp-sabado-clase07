import matplotlib.pyplot as plt

manzanas = [1500,4500,5000,3375,900]
nombres = ["Productos","Gastos","Ganancias","Distribución","Impuestos" ]
plt.pie(manzanas, labels=nombres, autopct="%0.1f S/")
plt.axis("equal")
plt.show()