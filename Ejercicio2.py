#Ejercicio2
class Papeleria:
    def __init__(self,nombre,marca,preCompra):
        self.nombre=nombre
        self.marca=marca
        self.preCompra=preCompra
        self.preVenta=self.PrecioVenta()
    
    def PrecioVenta(self):
        return round(self.preCompra * 1.30,2)
    
    def mostrarDatos(self):
        print(f"Articulo: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: {self.preCompra}")
        print(f"Precio de Venta: {self.preVenta}")
        print("************************")

class Cuaderno(Papeleria):
    def __init__(self,hojas,preCompra):
        self.hojas=hojas
        nombre = f"Cuaderno de {hojas} hojas"
        super().__init__(nombre,"Hojitas",preCompra)
        
class Lapiz(Papeleria):
    def __init__(self, tipo, preCompra):
        self.tipo=tipo
        nombre = f"Lapiz de {tipo}"
        super().__init__(nombre, "Rayas", preCompra)

def IngresarArticulos():
    print("Datos de los cuadernos")
    precioC50=float(input("Precio de compra del cuaderno de 50 hojas: "))
    cuaderno1 = Cuaderno(50, precioC50)
    
    precioC100=float(input("Precio de compra del cuaderno de 100 hojas: "))
    cuaderno2= Cuaderno(100, precioC100)
    
    print("\nDatos de los Lapices")
    grafito=float(input("Precio de compra del lapiz de grafito: "))
    lapiz1 = Lapiz("grafito", grafito)
    
    color=float(input("Precio de compra del lapiz de colores: "))
    lapiz2 = Lapiz("colores", color)
    
    print("\nCuadernos:")
    cuaderno1.mostrarDatos()
    cuaderno2.mostrarDatos()
    
    print("Lapices")    
    lapiz1.mostrarDatos()
    lapiz2.mostrarDatos()
    
IngresarArticulos()
    
    