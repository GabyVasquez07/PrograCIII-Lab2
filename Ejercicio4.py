# Ejercicio4
class Dispositivos:
    def __init__(self, tipo,marca,modelo,año,memoria,color,precio_compra):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.memoria= memoria
        self.color = color
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
        
    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.7,2)
    
    def mostrarDatos(self):
        print("*******************************")
        print(f"Dispositivo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Memoria: {self.memoria}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("*******************************")
        
def Registrar():
    cantidadDispositivos = int(input("¿Cuántos dispositivos desea registrar? "))
    dispositivos = []

    for i in range(cantidadDispositivos):
        print(f"\nRegistrar dispositivo {i + 1}:")
        tipo = input("Tipo de dispositivo (celular/tablet/laptop): ").lower()
        marca = "PHR"
        modelo = input("Modelo: ")
        año = input("Año: ")
        memoria = input("Memoria: ")
        color = input("Color: ")
        precio_compra = float(input("Precio de compra: "))

        dispositivo = Dispositivos(tipo, marca, modelo, año, memoria, color, precio_compra)
        dispositivos.append(dispositivo)
    
    for i, dispositivo in enumerate(dispositivos, start=1):
        print(f"\nDatos del dispositivo {i}:")
        dispositivo.mostrarDatos()


Registrar()
