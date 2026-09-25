"""Create,Read,Update,Delete
Registrar un listado de edades
"""
edades = []

def agregarEdad(edad):
    edades.append(edad)

def mostrarEdades():
    return edades

def actualizarEdad(index, edad):
    edades[index] = edad

def eliminarEdad(edad):
    edades.remove(edad)

def menu():
    print("1. Agregar edad")
    print("2. Editar edad")
    print("3. Eliminar edad")
    print("4. Mostrar edades")
    print("0. Salir")
    digito = input("Ingrese una opción: ")
    return digito

def pedirDato():
    edad = 0
    while True:
        try:
            dato = int(input(""))
            return dato
        except ValueError:
            print("Escribe un valor valido")

def seleccionarOpcion():
    op = menu()
    if op == "1":
        print("Dime una edad")
        edad = pedirDato()
        agregarEdad(edad)
    elif op == "2":
        print("Dime la posición de la edad a editar")
        pos = pedirDato()
        print("Dime la nueva edad")
        edad = pedirDato()
        actualizarEdad(pos, edad)
    elif op == "3":
        print("Dime la edad para eliminar")
        edad = pedirDato()
        eliminarEdad(edad)
        
    elif op == "4":
        print(mostrarEdades())
    
    elif op == "0":
        print("Saliendo del programa")
        return 0
    
        
    else:
        print("Opción no valida")
        

seleccionarOpcion()

def main():
    seleccionarOpcion()
main()