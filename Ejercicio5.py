#Ejercicio5 creado por mi
#registro de clientes de una cafeteria 

class Cliente:
    def __init__(self, nombre, edad, telefono, direccion, preferencia_bebida):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.preferencia_bebida = preferencia_bebida
        self.estado = "Activa"  # Por defecto, la cuenta está activa

    def mostrar_datos(self):
        print("*******************************")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print(f"Preferencia de bebida: {self.preferencia_bebida}")
        print(f"Estado: {self.estado}")
        print("*******************************")
        
def RegistrarCliente():
    cantidad_clientes = int(input("¿Cuántos clientes desea registrar? "))
    clientes = []

    for i in range(cantidad_clientes):
        print(f"\nRegistrar cliente {i + 1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        telefono = input("Número de teléfono: ")
        direccion = input("Dirección: ")
        preferencia_bebida = input("Preferencia de bebida: ")

        # Crear un objeto Cliente con los datos ingresados
        cliente = Cliente(nombre, edad, telefono, direccion,  preferencia_bebida)
        clientes.append(cliente)
    
    # Mostrar datos de los clientes registrados
    for i, cliente in enumerate(clientes, start=1):
        print(f"\nDatos del cliente {i}:")
        cliente.mostrar_datos()

RegistrarCliente()


