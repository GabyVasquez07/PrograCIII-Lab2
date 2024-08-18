#Ejercicio3
class Autos:
    def __init__(self,origen, marca, modelo, año, color, motor, transmision, combustible, precio_compra,  kilometros):
        self.origen = origen  
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.transmision = transmision  
        self.combustible = combustible
        self.precio_compra = precio_compra
        self.kilometros = kilometros
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4
        self.capacidad_pasajeros = 5
    
    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.4, 2)
    
    def mostrarDatos(self):
        print("*******************************")
        print(f"Origen: {self.origen}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Combustible: {self.combustible}")
        print(f"Kilómetros recorridos: {self.kilometros} km")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Número de ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print("*******************************")

def Registrar():
    cantidadAutos = int(input("¿Cuántos autos desea registrar? "))
    autos = []

    for i in range(cantidadAutos):
        print(f"\nRegistrar vehículo {i + 1}:")
        origen = input("Origen del vehículo (Nacional/Importado): ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        color = input("Color: ")
        motor = input("Motor: ")
        transmision = input("Transmisión (Manual/Automática): ")
        combustible = input("Combustible (Gasolina/Diésel/Eléctrico/Híbrido): ")
        precio_compra = float(input("Precio de compra: "))
        kilometros= float(input("Kilómetros recorridos: "))

        auto = Autos(origen, marca, modelo, año, color, motor, transmision, combustible, precio_compra,  kilometros)
        autos.append(auto)
    
    for i, auto in enumerate(autos, start=1):
        print(f"\nDatos del vehículo {i}:")
        auto.mostrarDatos()

Registrar()
    
