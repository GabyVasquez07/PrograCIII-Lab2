#ejericcio1
class VetPerros:
    def __init__(self, nombre, edad, raza, peso, pelaje, color, sexo, tipo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.pelaje = pelaje
        self.color = color
        self.sexo = sexo
        self.tipo = tipo
        self.Estado = "No atendido"
        self.dueño = None
        self.direccion = None
        self.telefono = None
    
    def Registrado(self):
        self.Estado = "Atendido"
        return self
        
    def datosDueño(self, dueño, direccion, telefono):
        self.dueño = dueño
        self.direccion = direccion
        self.telefono = telefono

    def mostrarDatos(self):
        print("*******************************")
        print("*****Nuevo registro*****")
        print()
        print(f"Información del Perro:\nNombre: {self.nombre}\nEdad: {self.edad} ")
        print(f"Raza: {self.raza}\nPeso: {self.peso} kg \nTipo: {self.tipo}")
        print(f"Color: {self.color}")
        print()
        print(f"Informacion del Dueño:\nNombre: {self.dueño} \nTelefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")
        print()
        print(f"Estado: {self.Estado}")
    
def IngresarDatos():
    print("Registrar Perro")
    nombre = input("Nombre del perro: ")
    edad = input("Edad del perro: ")
    raza = input("Raza del perro: ")    
    peso = float(input("Peso del perro(kg): "))
    if (peso<=10):
        tipo="Perro Pequeño"
    else:
        tipo="Perro Grande"
    pelaje=input("Tipo de pelaje (corto o largo): ")
    sexo=input("Ingrese el sexo del perro: ")
    color = input("Color del perro: ")    
    
    print("Datos del dueño")
    dueño = input("Nombre del dueño: ")
    telefono = input("Teléfono de emergencia: ")
    direccion= input("Dirección: ")
    
    datos = VetPerros(nombre,edad,raza,peso,pelaje,color,sexo,tipo)
    datos.Registrado()
    datos.datosDueño(dueño, direccion, telefono)
    
    datos.mostrarDatos()


IngresarDatos()
    
    